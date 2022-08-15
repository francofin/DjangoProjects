from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import user_register


urlpatterns = [
    path('login/', LoginView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('register/', user_register, name='register'),
]
