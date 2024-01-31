from django.contrib import admin

from muhammadamin.models import About, Post


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
