from django.contrib import admin
from django.urls import path,include
app_name = 'api'
from .views import artlist,artdet ,Userlist,Userdet,cat
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',artlist.as_view(),name = 'list'),
    path('<slug:slug>',artdet.as_view(),name = 'det'),
    path('user/',Userlist.as_view(),name = 'list'),
    path('user/<int:pk>',Userdet.as_view(),name = 'det'),
    path('token-auth/', obtain_auth_token),
    path('category/<slug:slug_cat>',cat,name = 'cat'),
]
