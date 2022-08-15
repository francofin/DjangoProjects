from distutils.command.clean import clean
from distutils.log import Log
from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post
from .forms import LoginForm, UserRegistrationForm, PostForm, PostUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def blog_list(request):
    posts = Post.objects.all().order_by('-published_at')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        post_set = paginator.page(page)
    except PageNotAnInteger:
        post_set = paginator.page(1)
    except EmptyPage:
        post_set = paginator.page(paginator.num_pages)

    
    context = {
        'posts':posts,
        'post_set':post_set,
        'page':page
    }
    return render(request, 'articles.html', context)

def post_details(request, slug):
    post = get_object_or_404(Post, slug = slug)
    context = {
        'post':post
    }

    return render(request, 'single_article.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request, username=cleaned_data['username'], password=cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HTTPResponse("You Are Authenticated")
            

            else:
                return HttpResponse("invalid Response")
                
    else:
        form = LoginForm()

    context = {
        'form':form
    }
    return render(request, 'login.html', context)


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # Dp not commit to be order to savbe passwords
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()


            return render(request, "register.html", {'form':user_form})

    else:
        user_form = UserRegistrationForm()
    return render(request, "register.html", {'form':user_form})


def post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('blog_list')
    else:
        post_form = PostForm()

    context = {
        'post_form':post_form
    }
    return render(request, 'add_article.html', context) 

@login_required
def update_post(request, slug):
    
    post = get_object_or_404(Post, slug=slug)
    post_Update_form = PostUpdateForm(request.POST or None, request.FILES or None, instance=post)
    
    if post_Update_form.is_valid():
        post_Update_form.save()
        return redirect('blog_list')

    context = {
        "post_Update_form":post_Update_form
    }
    return render(request, 'update_article.html', context)


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('blog_list')