from django.contrib import admin
from blogs.models import *


# Register your models here.

class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'views')


class AdminTag(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)


admin.site.register(Category)
admin.site.register(CategoryByZone)
admin.site.register(Tag, AdminTag)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(Post, AdminPost)
