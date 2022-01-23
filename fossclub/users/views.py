from django.shortcuts import render


@login_required
def profile(request):
    user = request.user
    context["user"] = user
    return render(request, "users/profile.html", context)
