from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Articl
from django.shortcuts import get_object_or_404
class Articllist(ListView):
    def get_queryset(self):
        return Articl.objects.all()
class artdet(DetailView):
    def get_object(self):
        return get_object_or_404(
            Articl,
            pk = self.kwargs.get('pk')
        )