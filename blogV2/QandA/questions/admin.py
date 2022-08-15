from django.contrib import admin
from .models import Question, Answer
# Register your models here.


@admin.register(Question)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_at')
    date_hierarchy= 'created_at'
    search_fields=( 'title', 'author')

@admin.register(Answer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('question', 'author','created_at')
    date_hierarchy= 'created_at'
    search_fields=( 'question', 'author')