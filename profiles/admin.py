from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from profiles.models import Post, SNUser


class PostAdmin(admin.ModelAdmin):
    list_display = ('message', 'file_type', 'posttime', 'edittime')

admin.site.register(Post, PostAdmin)

admin.site.register(SNUser, UserAdmin)