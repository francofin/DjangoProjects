from django.urls import path, include
from .views import UserViewSet, UserProfileViewSet, get_current_user, is_on_watch_list,\
update_user, register, update_user_profile, get_current_user_profile, add_stock_to_watchlist, get_user_portfolio
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
    path('myprofile/', get_current_user_profile, name='get_current_user_profile'),
    path('updateuserprofile/', update_user_profile, name='updateuserprofile'),
    path('addtowatchlist/<str:ticker>/', add_stock_to_watchlist, name='add_to_watchlist'),
    path('get_portfolio/', get_user_portfolio, name='get_user_portfolio'),
    path('stockonwatchlist/<str:ticker>/verify/', is_on_watch_list, name='is_on_watch_list'),
]