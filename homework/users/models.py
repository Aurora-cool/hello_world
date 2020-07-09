from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """自定义用户模型类"""

    # 额外增加 mobile 字段
    mobile = models.CharField(max_length=11,
                              unique=True,
                              verbose_name='手机号')
    # 新增 email_active 字段
    # 用于记录邮箱是否激活, 默认为 False: 未激活
    email_active = models.BooleanField(default=False,
                                       verbose_name='邮箱验证状态')

    # 补充默认地址字段:允许为空的，因为有些用户不去指定默认地址
    default_address_id = models.CharField(max_length=50, verbose_name='地址id', null=True)

    # 对当前表进行相关设置:
    class Meta:
        db_table = 'tb_users'

    # 在 str 魔法方法中, 返回用户名称
    def __str__(self):
        return self.username
