"""theClassified URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('store.urls')),
    path('', include('jobs.urls')),
    path('', include('stockuploader.urls')),
    path('', include('fintank_screener.urls')),
    path('', include('journal.urls')),
    path('', include('news.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


handler500 = 'utils.error_views.handler500'
handler404 = 'utils.error_views.handler404'