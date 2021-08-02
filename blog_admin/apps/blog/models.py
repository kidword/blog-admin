from django.db import models
from utils.models import BaseModel
from apps.system.models import User
# Create your models here.


# 文章分类表
class Category(BaseModel):
    name = models.CharField(max_length=50, verbose_name="名称")
    is_nav = models.BooleanField(default=True, verbose_name="是否为导航")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "文章分类表"


# 文章标签表
class Tag(BaseModel):
    name = models.CharField(max_length=50, verbose_name="名称")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "文章标签表"


# 文章表
class Article(BaseModel):
    title = models.CharField(max_length=255, verbose_name="文章标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文为markdown格式")
    content_type = models.IntegerField(default=1, verbose_name="文章格式类型")
    category = models.ForeignKey(Category, verbose_name="文章分类", on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name="文章标签")
    owner = models.ForeignKey(User, verbose_name="文章作者", on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = "文章表"
        ordering = ['-id']   # 根据id进行降序排列
