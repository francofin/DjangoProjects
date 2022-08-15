from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','published_at')
    date_hierarchy= 'published_at'
    search_fields=( 'title', 'description')
# admin.site.register(Post)
