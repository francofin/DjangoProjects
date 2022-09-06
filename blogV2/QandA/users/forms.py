from distutils.command.clean import clean
from distutils.command.upload import upload
from django import forms
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()



class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget = forms.PasswordInput)
    about = forms.Textarea()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'about')


    def clean_confirm_password(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['confirm_password']:
            raise forms.ValidationError("Passwords do not match")
        else:
            return clean_data['confirm_password']


class ProfileForm(forms.ModelForm):
    about = forms.Textarea()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'profile_picture', 'about')


