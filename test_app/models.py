# coding=utf-8
from django.db import models


# Create your models here.
class User(models.Model):
    """用户模型"""
    # 用户名
    username = models.CharField("用户名", max_length=50, unique=True, null=False)
    # 密码
    pwd = models.CharField("密码", max_length=100, null=False)
    # 邮箱
    email = models.CharField("邮箱", max_length=100, null=False)
    # 0为超级管理员，1为普通用户
    role = models.IntegerField("角色", default=1)
    # 激活状态
    is_active = models.BooleanField("用户是否激活", default=False)
    # 注册时间
    reg_time = models.DateTimeField("用户注册时间", auto_now_add=True)

    # # 自定义表
    # class Meta:
    #     db_table = "user"
    #     ordering = ["+/-按关键字排序",[...]]

    def __str__(self):
        return f"{self.id}:{self.username}"
