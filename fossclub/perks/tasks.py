import logging
import requests
from allauth.socialaccount.models import SocialAccount
from huey.contrib.djhuey import periodic_task, task

from .models import Badge, BadgeProgress


logger = logging.getLogger(__name__)


@task()
def check_followers_badge(user):
    # TODO: add GitLab followers check

    gh_account = SocialAccount.objects.filter(provider="github", user=user).first()

    if gh_account is None:
        raise Exception("GitHub is not connected for this user")

    for badge in Badge.objects.filter(unit="followers"):
        bp, _created = BadgeProgress.objects.get_or_create(user=user, badge=badge)
        bp.progress = min(badge.max_progress, gh_account.extra_data.get("followers", 0))
        bp.save()


@task()
def check_oauth_badge(user):
    social_accounts = SocialAccount.objects.filter(user=user)
    for social_account in social_accounts:
        badge = Badge.objects.filter(unit__iendswith=f" oauth").first()
        if badge is None:
            continue

        bp, _created = BadgeProgress.objects.get_or_create(user_id=user.id, badge_id=badge.id)
        bp.progress = badge.max_progress
        bp.save()


@task()
def check_commits_badge(user):
    commit_badges = Badge.objects.filter(unit__istartswith="commits in ")
    for badge in commit_badges:
        repo = badge.unit[len("commits in "):]
        if repo.lower().endswith(" on gitlab"):
            provider = "gitlab"
            repo = repo[:len(repo) -  len(" on gitlab")]
        elif repo.lower().endswith(" on github"):
            provider = "github"
            repo = repo[:len(repo) -  len(" on github")]
        else:
            provider = "github"

        social_account = SocialAccount.objects.filter(user=user, provider=provider).first()
        if social_account:
            if provider == "github":
                username = social_account.extra_data.get("login")
            elif provider == "gitlab":
                username = social_account.extra_data.get("username")
        else:
            logger.error("User is not connected with the required provider")
            continue

        try:
            commits = get_user_commits(username, repo, provider)
        except Exception as e:
            logger.exception(e)
        else:
            bp, _created = BadgeProgress.objects.get_or_create(user=user, badge=badge)
            if bp.unlocked == False:
                bp.progress = min(badge.max_progress, len(commits))
                bp.save()


def get_user_commits(username, repo, provider):
    if provider == "gitlab":
        commits = get_gitlab_commits(repo, username)
    elif provider == "github":
        commits = get_github_commits(repo, username)
    else:
        raise Exception(f"Unknown provider {provider}")

    return commits


def get_gitlab_commits(repo, author):
    pass


def get_github_commits(repo, author):
    url = f"https://api.github.com/repos/{repo}/commits"
    print("url: ", url)

    r = requests.get(url, headers={"Accept": "application/json"}, params={"author": author, "per_page": 100})
    if r.status_code == 404:
        raise Exception("Repo not found")

    return r.json()
