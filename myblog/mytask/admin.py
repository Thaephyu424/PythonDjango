from django.contrib import admin
from .models import *

# class MyBlogAdmin(admin,ModelAdmin):
#     list_display = ('Category','title','created_date')
# Register your models here.
admin.site.register(Category)
admin.site.register(MyBlog)
