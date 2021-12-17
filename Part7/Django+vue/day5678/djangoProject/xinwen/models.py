from django.db import models
from datetime import datetime

class xinwen(models.Model):
    biaoti = models.CharField(max_length=100, verbose_name=u"标题")#设置能够输出的最大值
    zuozhe = models.CharField(max_length=20, verbose_name=u"作者")  # 设置能够输出的最大值
    neirong = models.CharField(max_length=1000, verbose_name=u"内容")
    img_url = models.ImageField(upload_to='img_url/',verbose_name=u"图片地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")