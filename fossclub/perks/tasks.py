from allauth.socialaccount.models import SocialAccount
from huey.contrib.djhuey import periodic_task, task

from .models import Badge, BadgeProgress


@task()
def check_followers_badge(user):
    try:
        gh_account = SocialAccount.objects.filter(provider="github", user=user).first()
    except SocialAccount.DoesNotExist:
        raise Exception("GitHub is not connected for this user")

    for badge in Badge.objects.filter(unit="followers"):
        bp, _created = BadgeProgress.objects.get_or_create(user=user, badge=badge)
        bp.progress = min(badge.max_progress, gh_account.extra_data.get("followers", 0))
        bp.save()


@task()
def check_oauth_badge(user):
    social_accounts = SocialAccount.objects.filter(user=user)
    for social_account in social_accounts:
        badge = Badge.objects.filter(unit=f"{social_account.provider}_oauth").first()
        if badge is None:
            continue

        bp, _created = BadgeProgress.objects.get_or_create(user_id=user.id, badge_id=badge.id)
        bp.progress = badge.max_progress
        bp.save()

@task()
def check_commits_badge(user):
    pass
