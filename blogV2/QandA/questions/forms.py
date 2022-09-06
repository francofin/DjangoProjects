
from distutils.command.clean import clean
from distutils.command.upload import upload
from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User



class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body','image1', 'image2', 'image3',)

class QuestionUpdateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body','image1', 'image2', 'image3',)

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('body', 'image1', 'image2', 'image3',)

class AnswerUpdateForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('body', 'image1', 'image2', 'image3',)

# class PostUpdateForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('title', 'description', 'image')

# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')    
#     class Meta:
#         model = Images
#         fields = ('image', )
    