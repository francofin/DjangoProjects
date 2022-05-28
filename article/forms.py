from django import forms
from django.contrib.auth.models import User
from .models import Article


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

class UserRegistration(forms.ModelForm):

    password = forms.CharField(label="Password", widget = forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget = forms.PasswordInput)
    about_me = forms.Textarea()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_confirm_password(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['confirm_password']:
            raise forms.ValidationError("Passwords do not match")
        else:
            return clean_data['confirm_password']


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description')


class ArticleUpdateForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'description')