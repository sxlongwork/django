from django.contrib import admin
from booktest.models import *

# Register your models here.
# 后台管理


class BookInfoAdmin(admin.ModelAdmin):
    """自定义管理模型类，用来控制在管理页面的展示内容"""
    list_display = ["id", "title", "pub_data"]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", 'sex', "book"]


# 注册模型类,可以在管理台管理数据库数据

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)