from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from perks.models import Perk, Badge


def list_perks(request):
    # TODO: add pagination

    context = {}

    if request.user.is_authenticated:
        context["perks_won"] = request.user.perks_won.all()
        context["perks"] = Perk.objects.exclude(id__in=context["perks_won"])
    else:
        context["perks"] = Perk.objects.all()

    return render(request, "perks/list.html", context)


@login_required
def list_badges(request):
    context = {}

    # TODO: this can be optimised, but come to this later

    locked_badges = request.user.locked_badges
    unlocked_badges = request.user.unlocked_badges
    badge_progresses = request.user.badgeprogress_set.all()

    context["locked_badges"] = []

    for badge in locked_badges:
        badge_progress = None
        for bp in badge_progresses:
            if badge == bp.badge:
                badge_progress = bp
                break

        context["locked_badges"].append((badge, badge_progress))

    context["unlocked_badges"] = unlocked_badges

    return render(request, "perks/badges.html", context)
