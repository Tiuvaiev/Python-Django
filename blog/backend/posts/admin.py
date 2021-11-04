from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['id', 'title', 'content', 'author']
    readonly_fields = ('id',)
