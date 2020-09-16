from django.db import models

# Create your models here.
typelist = [(1, 'web服务器'), (2, '数据库服务器'), (3, '缓存服务器')]
statuslist = [(0, 'offline'), (1, 'online')]


class Host(models.Model):
    hostname = models.CharField(max_length=32, verbose_name='服务器名称')
    ip = models.CharField(max_length=15, verbose_name='服务器ip地址')
    type = models.IntegerField(verbose_name='服务器类型', choices=typelist)
    status = models.IntegerField(default=0, verbose_name='服务器状态', choices=statuslist)

    class Meta:
        db_table = 'hostlist'
        verbose_name = '服务器信息列表'


class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name='图书名称')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='图书价格')
    publish = models.ForeignKey('Publish', null=True, on_delete=models.SET_NULL)
    author = models.ManyToManyField('Author')

    class Meta:
        db_table = 'book'
        verbose_name = '图书信息'


class Publish(models.Model):
    name = models.CharField(max_length=20, verbose_name='出版社名称')
    address = models.CharField(max_length=50, verbose_name='出版社地址')

    class Meta:
        db_table = 'publish'
        verbose_name = '出版社信息'


class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='作者名字')
    job = models.CharField(max_length=20, verbose_name='作者职业')

    class Meta:
        db_table = 'author'
        verbose_name = '作者信息'
