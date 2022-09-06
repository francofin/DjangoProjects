from django.contrib import admin
from .models import CustomUser, UserProfile
# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','created_at', 'role')
    date_hierarchy= 'created_at'
    search_fields=( 'username', 'role')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','updated_at')
    date_hierarchy= 'updated_at'
    search_fields=( 'user',)