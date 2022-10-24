from django.contrib import admin
from .models import Journal
# Register your models here.

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('title', 'category', 'author', 'created_at')