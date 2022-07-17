from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ArticleViewSet
# article_list, article_details,ArticleDetail

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
# router.register('articles/<slug:slug>/', ArticleDetail, basename='details')
urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<slug:slug>/', article_details),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetail.as_view()),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<slug:slug>/', ArticleDetail.as_view()),
    path('', include(router.urls))
]
