from django.db import models

class xinwen(models.Model):
    biaoti = models.CharField(max_length=100)#设置能够输出的最大值
    zuozhe = models.CharField(max_length=20)  # 设置能够输出的最大值
    neirong = models.CharField(max_length=1000)
