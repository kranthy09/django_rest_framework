# serializers.py

from rest_framework import serializers
from .models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Hero
        fields = ('name', 'alias')
