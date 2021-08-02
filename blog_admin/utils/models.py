from django.db import models
import django.utils.timezone as timezone


class BaseModel(models.Model):
    """
    基本表
    """
    create_time = models.DateTimeField(
        default=timezone.now, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(
        auto_now=True, verbose_name='修改时间', help_text='修改时间')
    is_deleted = models.BooleanField(
        default=False, verbose_name='删除标记', help_text='删除标记')

    class Meta:
        abstract = True
