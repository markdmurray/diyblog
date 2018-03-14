from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=400, help_text="Enter your bio detailes here")

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    comments = models.TextField(max_length=2000, help_text="Enter your blog text here")
    post_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000, help_text="Enter your comment here")

    def __str__(self):
        return self.description