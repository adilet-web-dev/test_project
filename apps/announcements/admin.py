from django.contrib import admin

from .models import Category, Subcategory, Announcement
# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Announcement)
