from django.db import models

# Create your models here.


class BookInfoManager(models.Manager):
    """自定义图书管理器"""
    # 自定义管理器的两种应用场景
    # 1.修改原有的查询集，如all()
    def all(self):
        # 调用父类的all方法
        books = super().all()
        # 对结果集进行过滤
        books = books.filter(is_delete=0)
        return books

    # 2.添加额外的方法
    def create_book(self, name, pub_date):
        # 1.获取模型类,创建模型类对象
        model_class = self.model        # 获取管理器对象对应的模型类
        book = model_class()            # 根据模型类创建模型对象
        # 2.设置对象属性，保存数据
        book.name = name
        book.pub_date = pub_date
        book.save()
        return book


class BookInfo(models.Model):
    """图书信息模型类"""
    # 图书名称
    name = models.CharField(max_length=20)
    # 图书发布日期
    pub_date = models.DateField()
    # 图书阅读量
    read = models.IntegerField(default=0)
    # 图书评论数
    comment = models.IntegerField(default=0)
    # 删除标记
    is_delete = models.BooleanField(default=False)
    # 自定义管理器对象
    objects = BookInfoManager()

    def __str__(self):
        return self.name


class HeroInfo(models.Model):
    """英雄信息模型类"""
    # 英雄名称
    name = models.CharField(max_length=20)
    # 性别
    sex = models.BooleanField(default=False)
    # 备注，英雄说明信息
    comment = models.CharField(max_length=50)
    # 关系属性
    book = models.ForeignKey("BookInfo")

    def __str__(self):
        return self.name


class User(models.Model):
    """用户信息"""
    name = models.CharField(max_length=40)
    sex = models.BooleanField(default=False)
    age = models.IntegerField(null=True, default=None)
    birth = models.DateField(null=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    comment = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name

