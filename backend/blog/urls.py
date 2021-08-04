from django.contrib import admin
from django.urls import path,include
app_name = 'blog'
from .views import Articllist,artdet
urlpatterns = [
    path('',Articllist.as_view(),name = 'list'),
    path("<int:pk>",artdet.as_view(),name = 'det')
]
