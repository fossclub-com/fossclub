from .models import Badge

badges = [
    {"name": "Rockstar I", "image": "badges/rockstar50.png", "short_description": "Have 50 followers on GitHub", "max_progress": 50, "unit": "followers"},
    {"name": "Rockstar II", "image": "badges/rockstar100.png", "short_description": "Have 100 followers on GitHub", "max_progress": 100, "unit": "followers"},
    {"name": "Rockstar III", "image": "badges/rockstar500.png", "short_description": "Have 500 followers on GitHub", "max_progress": 500, "unit": "followers"},
    {"name": "Rockstar IV", "image": "badges/rockstar1000.png", "short_description": "Have 1000 followers on GitHub", "max_progress": 1000, "unit": "followers"},
    {"name": "Indie Creator I", "image": "badges/indie_creator50.png", "short_description": "Owner of a project with 50+ stars", "max_progress": 50, "unit": "stars"},
    {"name": "Indie Creator II", "image": "badges/indie_creator100.png", "short_description": "Owner of a project with 100+ stars", "max_progress": 100, "unit": "stars"},
    {"name": "Indie Creator III", "image": "badges/indie_creator1000.png", "short_description": "Owner of a project with 1000+ stars", "max_progress": 1000, "unit": "stars"},
    {"name": "Indie Creator IV", "image": "badges/indie_creator10000.png", "short_description": "Owner of a project with 10000+ stars", "max_progress": 10000, "unit": "stars"},
    {"name": "GitHub Signin", "image": "badges/github_login.png", "short_description": "Have a GitHub account", "max_progress": 1, "unit": "GitHub OAuth"},
    {"name": "GitLab Signin", "image": "badges/gitlab_login.png", "short_description": "Have a GitLab account", "max_progress": 1, "unit": "GitLab OAuth"},
    {"name": "Tensorflow Contributor", "image": "badges/tensorflow_contributor.png", "short_description": "Have contributed to Tensorflow", "max_progress": 1, "unit": "commits in tensorflow/tensorflow"},
]

for badge_args in badges:
  Badge.objects.get_or_create(**badge_args)