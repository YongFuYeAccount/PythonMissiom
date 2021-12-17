# -*- coding: utf-8 -*-
#file location the same as spider
# author yyf
from rest_framework import serializers#模型引入
from .models import xinwen
class XinwenSerializer(serializers.ModelSerializer):
    class Meta:
        model = xinwen#模型是新闻
        fields = ["biaoti", "zuozhe", "neirong","img_url","add_time"]