from django.urls import path, include
from .views import UserViewSet, UserProfileViewSet, get_current_user, update_user, register
from rest_framework.routers import DefaultRouter
from theRest.urls import router as rest_router

router = DefaultRouter()
router.registry.extend(rest_router.registry)
router.register('users', UserViewSet, basename='users')
router.register('userprofiles', UserProfileViewSet, basename='userprofiles')


urlpatterns = [
    path('', include((router.urls, 'users'))),
    path('register/', register, name='register'),
    path('userprofile/', get_current_user, name='userprofile'),
    path('updateprofile/', update_user, name='updateprofile'),
]