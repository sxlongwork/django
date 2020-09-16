from django.db import models

# Create your models here.

# 设计和表对应额模型类
# 所有模型类都要继承models.Model类


class BookInfo(models.Model):
    """图书类模型"""
    # 图书名称 CharField说明是一个字符串，max_length指定字符串最大长度
    title = models.CharField(max_length=20)
    # 图书出版日期 DateField说明是一个日期类型
    pub_data = models.DateField()

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    "英雄人物模型"
    name = models.CharField(max_length=20)
    sex = models.IntegerField()
    # 定义关系属性，英雄为book中的任务，1对多的关系
    book = models.ForeignKey("BookInfo")
