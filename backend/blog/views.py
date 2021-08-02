from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

class Articlelist(ListView):
    def get_queryset(self):
        return Article.objects.all()