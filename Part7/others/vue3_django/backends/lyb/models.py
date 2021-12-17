from django.db import models

# Create your models here.
class Lyb(models.Model):#留言的内容
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    cotent = models.TextField()
    posttime =models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table ="d_lyb"#表格的名字
