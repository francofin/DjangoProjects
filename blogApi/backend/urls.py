from django.contrib import admin
from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


# for viewset
router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')


urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details),
    path('', include(router.urls)),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetail.as_view()),
]
