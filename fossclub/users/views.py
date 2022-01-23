from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profile(request):
    context = {}
    user = request.user

    context["user"] = user
    return render(request, "users/profile.html", context)
