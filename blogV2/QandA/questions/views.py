from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from .models import Question, Answer
from .forms import AnswerForm, QuestionForm, QuestionUpdateForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
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
    answers = Answer.objects.filter(question=question)

    if request.method == 'POST':
    
        answerForm = AnswerForm(request.POST, request.FILES)
        print(request.POST)
        if answerForm.is_valid():
            answer_form = answerForm.save(commit=False)
            answer_form.author = request.user
            answer_form.question =question
            answer_form.save()
            # use django messages framework
            messages.success(request,"Thanks for contributing to our knowledge based community.")
            return HttpResponseRedirect("/")
        else:
            print(answerForm.errors)
    else:
        answerForm = AnswerForm()

    context = {
        'question':question,
        'answerForm':answerForm,
        'answers':answers
    }

    return render(request, 'question-detail.html', context)

@login_required
def update_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question_Update_form = QuestionUpdateForm(request.POST or None, request.FILES or None, instance=question)

    if question_Update_form.is_valid():
        question_Update_form.save()
        return redirect('question_detail', slug=question.slug)

    context = {
        "question_Update_form":question_Update_form
    }
    return render(request, 'profile-pages/update-detail.html', context)

@login_required
def delete_question(request, slug):
    question = get_object_or_404(Question, slug=slug)
    question.delete()
    return redirect('question_list')


@login_required
def user_questions(request):
    questions = Question.objects.filter(author = request.user)

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
    return render(request, 'profile-pages/userprofile.html', context)

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
