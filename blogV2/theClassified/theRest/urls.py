from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter
# from users.views import UserProfileViewSet, UserViewSet
# post_list, post_detail

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
# router.register('users', UserViewSet, basename='users')
# router.register('userprofiles', UserProfileViewSet, basename='userprofiles')
urlpatterns = [
    path('', include(router.urls))
    # path('posts/', PostList.as_view()),
    # path('posts/<slug:slug>', PostDetail.as_view()),
    # path('posts/', post_list),
    # path('post/<slug:slug>', post_detail),
]