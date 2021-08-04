from rest_framework import serializers
from blog.models import Articl
from django.contrib.auth.models import User

class artserializer(serializers.ModelSerializer):
    class Meta:
        model = Articl
        # exclude = ('created','updated')
        fields = "__all__"
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # exclude = ('created','updated')
        fields = "__all__"