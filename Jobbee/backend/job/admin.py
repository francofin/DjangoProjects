from django.contrib import admin
from .models import Job
# Register your models here.

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'industry', 'user', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('title', 'user', 'industry', 'company')