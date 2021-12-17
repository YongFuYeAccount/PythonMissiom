"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

from xinwen.views import XinwenViews
router.register(r'xinwen', XinwenViews, basename='xinwen')#配置的功能页面
urlpatterns = [
    url('admin/', admin.site.urls),
    url('2222/', include(router.urls)),#''里面可以隐藏一定的地址主网站地址
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

