from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class category(models.Model):
    title = models.CharField(max_length=200)
    slug_cat = models.SlugField(max_length=100,)
    status =models.BooleanField(default=True,)
    def __str__(self):
        return self.title
class Articl(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    publish = models.DateTimeField(default= timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(category)
    def __str__(self):
        return self.title
