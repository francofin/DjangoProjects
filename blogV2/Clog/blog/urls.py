from django.contrib import admin
from django.urls import path
from .views import blog_list, user_login, user_register, post_form, post_details, update_post, delete_post
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('',blog_list, name='blog_list'),
    # path('login/', user_login, name='user_login'),
    path('posts/<slug:slug>/', post_details, name='post_details'),
    path('update-post/<slug:slug>/', update_post, name='update_post'),
    path('delete-post/<slug:slug>/', delete_post, name='delete_post'),
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('create-post/', post_form, name='post_form_create'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

]
