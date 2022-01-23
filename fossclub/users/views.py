from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect("/perks/")
    else:
        return redirect("/accounts/signup/")


@login_required
def profile(request):
    context = {}
    user = request.user

    context["user"] = user
    return render(request, "users/profile.html", context)
