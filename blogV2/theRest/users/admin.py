from django.contrib import admin
from .models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','date_joined', 'role')
    date_hierarchy= 'date_joined'
    search_fields=( 'username', 'role')