
from django.shortcuts import render
from .serializers import XinwenSerializer#引入组件的内容
from .models import xinwen#引入模型

from rest_framework import viewsets

class XinwenViews(viewsets.ModelViewSet):
    serializer_class = XinwenSerializer
    def get_queryset(self):
        return xinwen.objects.all()#返回新闻对应的数据包