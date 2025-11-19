from django.db import models
import uuid
from django.db.models import ForeignKey

class Department(models.Model):
    title=models.CharField(verbose_name='部门',max_length=32)
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name=models.CharField(verbose_name='名字',max_length=32)
    password=models.CharField(verbose_name='密码',max_length=32)
    age=models.IntegerField(verbose_name='年龄')
    account=models.IntegerField(verbose_name='工资')
    create_time=models.DateTimeField(verbose_name='入职时间',auto_now_add=True)

    depart=ForeignKey(verbose_name='部门id',to='Department',to_field='id',on_delete=models.CASCADE)
    # 非级连删除
    # depart1=ForeignKey(verbose_name='部门id',to='Department',to_field='id',blank=True,on_delete=models.SET_NULL)

    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choice)