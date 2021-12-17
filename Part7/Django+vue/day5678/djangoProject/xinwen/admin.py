from django.contrib import admin
from .models import xinwen

class XinwenAdmin(admin.ModelAdmin):
    list_display = ["biaoti","zuozhe","neirong"]#不能有空格


admin.site.register(xinwen,XinwenAdmin)#前面写模型名称，后面写命名的组件配置

