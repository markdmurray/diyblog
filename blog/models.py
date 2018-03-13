from django.db import models
from django.contrib.auth import User

# Create your models here.

class Author(models.Model):
    name = models.ForeignKey(User, )
    bio =

class Blog(models.Model):


class BlogComment(models.Model):
