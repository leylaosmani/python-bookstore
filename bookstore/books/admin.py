from django.contrib import admin

# Import models in current application folder
from .models import Book

# Register your models here.

# Register movie model in admin panel
admin.site.register(Book)


