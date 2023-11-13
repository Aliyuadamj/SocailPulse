from django.contrib import admin

from .models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display=['first_name', 'email', 'created','updated']
admin.site.register(Login, LoginAdmin)
