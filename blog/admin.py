from django.contrib import admin

from .models import Post

# Register your models here.


class Postsco(admin.ModelAdmin):
    list_display = [
        'title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status'
    ]


admin.site.register(Post, Postsco)
