from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.


def question_list(request):

    questions = Question.objects.all().order_by('-created_at')

    context = {
        'questions':questions
    }

    return render(request, 'home.html', context)


def question_details(request, slug):
    question = get_object_or_404(Question, slug=slug)

    context = {
        'question':question
    }

    return render(request, 'question_details.html', context)