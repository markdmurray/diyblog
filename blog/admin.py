from django.contrib import admin
from .models import Author, Blog, BlogComment

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(BlogComment)