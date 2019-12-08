from django.contrib import admin
from books.models import bookInfo,HeroInfo
# Register your models here.
#自定义模型管理类
class bookInfoAdmin(admin.ModelAdmin):
    '''图书管理类模型'''
    list_display = ['id','btitle','dbdate']
class HeroInfoAdmin(admin.ModelAdmin):
    '''英雄人物模型管理类'''
    list_display = ['id','hname','hcomment']


# 注册模型类
admin.site.register(bookInfo,bookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
