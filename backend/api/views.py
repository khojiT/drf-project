from django.shortcuts import render
from blog.models import Articl
from .serializers import artserializer,Userserializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
class artlist(ListCreateAPIView):
    queryset = Articl.objects.all()
    serializer_class  = artserializer

class artdet(RetrieveUpdateDestroyAPIView):
    queryset = Articl.objects.all()
    serializer_class  = artserializer
    lookup_field = 'slug'


class Userlist(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class  = Userserializer
    permission_classes = (IsAdminUser,)

class Userdet(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class  = Userserializer
    permission_classes = (IsAdminUser,)

# def cat(request,slug_cat):
#     queryset = Articl.objects.filter(category = ca)
#     lookup_field = 'slug_cat'


@api_view(['GET'])
def cat(request,slug_cat):
    artileee = Articl.objects.filter(category__slug_cat = slug_cat)
    serializer  = artserializer(artileee,many = True)
    return Response(serializer.data)