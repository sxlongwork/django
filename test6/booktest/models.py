from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=30, db_column='username'),
    passwd = models.CharField(db_column='password'),
    sex = models.IntegerField(max_length='10', db_column='sex', default=1),
    birth = models.DateField()
    class Meta():
        db_table = 't_user'
