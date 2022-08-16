from .views import delete_question, question_list, post_question, question_detail, user_questions, update_question, delete_question
from django.urls import path


urlpatterns = [
    path('', question_list, name='question_list'),
    path('post-question/', post_question, name='post_question'),
    path('question-detail/<slug:slug>', question_detail, name='question_detail'),
    path('update-detail/<slug:slug>', update_question, name='update_question'),
    path('delete-detail/<slug:slug>', delete_question, name='delete_question'),
    path('user-questions/', user_questions, name='user_questions'),
]
