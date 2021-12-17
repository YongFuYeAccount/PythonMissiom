from django.db import models
from datetime import datetime

class xinwen(models.Model):#用于设置django管理员页面上的增添内容时的提示
    biaoti = models.CharField(max_length=100, verbose_name=u"标题")#设置能够输出的最大值
    zuozhe = models.CharField(max_length=20, verbose_name=u"作者")  # 设置能够输出的最大值
    neirong = models.CharField(max_length=1000, verbose_name=u"内容")
    img_url = models.ImageField(upload_to=r'C:\Users\86182\Desktop\PythonMission\Part7\practice\djangoProject\upimg\img_url/',verbose_name=u"图片地址")
    #该图片所的绝对路径
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")