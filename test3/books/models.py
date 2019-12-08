from django.db import models
# Create your models here.
class bookInfo(models.Model):

    btitle = models.CharField(max_length=20)
    # 日期
    dbdate = models.DateField()

    def __str__(self):
        #返回书名
        return self.btitle

#多类
#英雄类
class feng(models.Model):
    fname = models.CharField(max_length=20)

    def __str__(self):
        # 返回书名
        return self.btitle
class fengying(models.Model):
    fname = models.CharField(max_length=20)
    dbdate = models.DateField()

    # 备注
    hcomment = models.CharField(max_length=128)

class Fengjsonobj():
    name = ""
    age = 0
    sex = ""

class HeroInfo(models.Model):
    #名  字符串
    hname = models.CharField(max_length=20)
    #性 别
    hgender = models.BooleanField(default=False)
    #备注
    hcomment = models.CharField(max_length=128)
    #关系属性 hbooK 建立图书类和英雄人类 之间的一对多的关系
    hbook = models.ForeignKey('bookInfo')
    def __str__(self):
        return self.hname