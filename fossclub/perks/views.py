from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

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

    locked_badges = request.user.locked_badges.order_by("max_progress")
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


def show_perk(request, perk_id):
    perk = get_object_or_404(Perk, id=perk_id)
    return render(request, "perks/show.html", context={"perk": perk})


class PerkCreateView(LoginRequiredMixin, CreateView):
    model = Perk
    fields = ["name", "short_description", "long_description", "image", "required_badges", "quantity"]
    template_name = "perks/new.html"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
