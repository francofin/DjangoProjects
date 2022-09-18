from django.urls import path
from .views import upload_template

urlpatterns = [
    path('upload/', upload_template, name='stock_uploader'),
]
