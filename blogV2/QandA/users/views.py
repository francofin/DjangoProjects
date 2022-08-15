from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import CustomUser

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