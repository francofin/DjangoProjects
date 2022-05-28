from django.urls import path, include
from .views import article_list, article_details, register, create_article_form, update_article_form, delete_article
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
urlpatterns = [
    path('', article_list, name='articles'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls',  namespace='social')),
    path('create-article/', create_article_form, name='create-article'),
    path('delete-article/<slug:slug>/', delete_article, name='delete-article'),
    path('update-article/<slug:slug>/', update_article_form, name='update-article'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('login/', user_login, name='login'),
    path('register/', register, name='register'),
]
