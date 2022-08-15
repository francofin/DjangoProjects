from .views import question_list, post_question, question_detail
from django.urls import path


urlpatterns = [
    path('', question_list, name='question_list'),
    path('post-question/', post_question, name='post_question'),
    path('question-detail/<slug:slug>', question_detail, name='question_detail'),
]
