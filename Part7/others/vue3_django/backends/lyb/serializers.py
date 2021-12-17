# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Lyb

# Serializers define the API representation.
class LybSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyb
        fields = "__all__"