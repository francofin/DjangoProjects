from django.urls import path, include
from . import views


urlpatterns = [
    path('journals/', views.get_all_journals, name='all_journals'),
    
]