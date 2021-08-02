from django.contrib import admin
from django.urls import path,include
app_name = 'blog'
from .views import Articlelist
urlpatterns = [
    path('',Articlelist.as_view(),name = 'list')
]
