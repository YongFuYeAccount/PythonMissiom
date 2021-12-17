from django.db import models

# Create your models here.
class imagefile(models.Model):
    imagename = models.ImageField(null=True,blank=True)
    labelnote = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
class Imagelabel(models.Model):
    imagename = models.CharField(max_length=100,null=True,blank=True)
    x1 = models.CharField(max_length=10,null=True,blank=True)
    y1 = models.CharField(max_length=10, null=True, blank=True)
    x2 = models.CharField(max_length=10, null=True, blank=True)
    y2 = models.CharField(max_length=10, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.CharField(max_length=100, null=True, blank=True)
    warn =  models.CharField(max_length=100, null=True, blank=True)

class User(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True)
    pwd = models.CharField(max_length=100, null=True, blank=True)
    authority = models.CharField(max_length=100,null=True,blank=True)

class Userimgae(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True)
    imagename = models.CharField(max_length=100, null=True, blank=True)
    labelnote = models.CharField(max_length=100, null=True, blank=True)


from django.contrib import admin
admin.site.register(imagefile)