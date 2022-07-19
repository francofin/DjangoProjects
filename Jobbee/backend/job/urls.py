from django.urls import path, include
from . import views


urlpatterns = [
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/<str:pk>/', views.getJob, name='job'),
    path('jobs/new/', views.newJob, name='new_job'),
    path('jobs/<str:pk>/update/', views.updateJob, name='update_job'),
    path('jobs/<str:pk>/delete/', views.deleteJob, name='delete_job'),
    path('stats/<str:topic>/', views.getTopicStats, name='job_stats'),
    path('jobs/<str:pk>/apply/', views.apply_to_job, name='apply_to_job'),
    path('me/jobs/applied/', views.get_applied_jobs, name='get_applied_jobs'),
]