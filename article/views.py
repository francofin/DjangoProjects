from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article
from .forms import LoginForm, UserRegistration, ArticleForm, ArticleUpdateForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.

def article_list(request):
    all_articles = Article.objects.all().order_by('-published')
    paginator = Paginator(all_articles, 3)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    
    context = {
        'all_articles':all_articles,
        'articles':articles,
        'page':page
    }
    return render(request, 'articles.html', context)

def article_details(request, slug):
    article = get_object_or_404(Article, slug = slug)
    context = {
        'article':article
    }

    return render(request, 'single_article.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cleaned_form_data = form.cleaned_data
            user = authenticate(request, username = cleaned_form_data['username'], password = cleaned_form_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('You are authenticated')
            else:
                return HttpResponse("Invalid Login Credentials")

    else:
        form = LoginForm()

    context = {
        'form':form
    }

    return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            context = {
                'user_form':user_form
            }
            return render(request, 'register.html', context)

    else:
        user_form = UserRegistration()

    context = {
        'user_form':user_form
    }

    return render(request, 'register.html', context)

@login_required
def create_article_form(request):
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        
        if article_form.is_valid():
            article = article_form.save(commit=False)

            article.author = request.user
            article.save()

            return redirect('articles')

    else:
        article_form = ArticleForm()
        

    context = {
        "article_form":article_form
    }
    return render(request, 'add_article.html', context)


@login_required
def update_article_form(request, slug):
    article = get_object_or_404(Article, slug=slug)

    article_Update_form = ArticleUpdateForm(request.POST or None, instance=article)
    
    if article_Update_form.is_valid():
        article_Update_form.save()
        return redirect('articles')

    context = {
        "article_Update_form":article_Update_form
    }
    return render(request, 'update_article.html', context)

@login_required
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article.delete()
    return redirect('articles')