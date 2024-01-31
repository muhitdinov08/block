from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstractBsedModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)


class Post(AbstractBsedModel):
    title = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title


class About(AbstractBsedModel):
    title = models.CharField(max_length=38)
    description = models.TextField()

    def __str__(self):
        return self.title


class Author(AbstractBsedModel):
    Choice_gender = [
        ('m', "Male"),
        ('f', "Female"),
    ]
    user_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=Choice_gender, null=True)
    age = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
