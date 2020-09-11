from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ("author", "title", "body", "created_at")


# admin.site.register(Post)
admin.site.register(Post, PostAdmin)
