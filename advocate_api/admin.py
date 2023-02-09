from django.contrib import admin

from .models import Advocate


class AdminAdvocate(admin.ModelAdmin):
    list_display = ['name', 'username', 'bio', 'profile_pic', 'twitter', 'joined_date']
    search_fields = ['usernmae', 'name']
    list_filter = ['username', 'joined_date']



admin.site.register(Advocate, AdminAdvocate)