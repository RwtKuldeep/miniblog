from django.contrib import admin
from .models import Post, User_Contact
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(User_Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'message']
