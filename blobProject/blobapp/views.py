from django.shortcuts import render, redirect
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def upload_profile_picture(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'upload_profile_picture.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile_view.html')


