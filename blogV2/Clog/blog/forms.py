
from distutils.command.clean import clean
from distutils.command.upload import upload
from django import forms
from .models import Post
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirmPassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password',  'confirmPassword')

    def cleaned_data(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['confirmPassword']:
            raise forms.ValidationError("Passowors do not match")

        return cleaned_data


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'description', 'image')

    