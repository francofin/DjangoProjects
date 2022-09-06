from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileForm
from .models import CustomUser
from django.contrib import messages


# Create your views here.
def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Dp not commit to be order to savbe passwords
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()


            return render(request, "registration-complete.html", {'form':user_form})

    else:
        user_form = UserRegistrationForm()
    return render(request, "register.html", {'form':user_form})


def change_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Has Been Up[dated")
    else:
        form = ProfileForm(instance = request.user)

    context = {
        'form':form
    }

    return render(request, 'profile-pages/account-detail.html', context)
