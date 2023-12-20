from django.shortcuts import render
from .models import Profile
from .forms import DweetForm
from django.shortcuts import render, redirect

# dwitter/views.py

from django.shortcuts import render

# dwitter/views.py

def dashboard(request):
    if request.method == "POST":
        form = DweetForm(request.POST)
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    form = DweetForm()
    return render(request, "dashboard.html", {"form": form})

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

# dwitter/views.py

# ...

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile.html", {"profile": profile})
