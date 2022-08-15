from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory
# Create your views here.


def question_list(request):
    questions  = Question.objects.all().order_by('-created_at')
    print([f.name for f in Question._meta.get_fields()])
    print(questions[0].__dict__)

    paginator = Paginator(questions, 3)
    page = request.GET.get('page')

    try:
        question_set = paginator.page(page)
    except PageNotAnInteger:
        question_set = paginator.page(1)
    except EmptyPage:
        question_set = paginator.page(paginator.num_pages)


    context = {
        'questions':questions,
        'question_set':question_set,
        'page':page
    }
    return render(request, "home.html", context)

def question_detail(request, slug):
    question = get_object_or_404(Question, slug=slug)

    if request.method == 'POST':
    
        answerForm = AnswerForm(request.POST, request.FILES)
        if answerForm.is_valid():
            answer_form = answerForm.save(commit=False)
            answer_form.author = request.user
            answer_form.save()
            # use django messages framework
            messages.success(request,"Thanks for contributing to our knowledge based community.")
            return HttpResponseRedirect("/")
        else:
            print(answerForm.errors)
    else:
        answerForm = QuestionForm()

    context = {
        'question':question,
        'answerForm':answerForm
    }

    return render(request, 'question-detail.html', context)


def post_question(request):

    if request.method == 'POST':
    
        questionForm = QuestionForm(request.POST, request.FILES)
    
        if questionForm.is_valid():
            question_form = questionForm.save(commit=False)
            question_form.author = request.user
            question_form.save()
            # use django messages framework
            messages.success(request,"Thanks for contributing to our knowledge based community.")
            return HttpResponseRedirect("/")
        else:
            print(questionForm.errors)
    else:
        questionForm = QuestionForm()


    context = {
        'questionForm':questionForm,
    }
    return render(request, 'postQuestion.html', context)
