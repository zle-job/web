
from django.db import models

# Create your models here.

from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="分类")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="标签")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    """
    博客
    """
    title = models.CharField(max_length=30, null=True, verbose_name="标题")
    time = models.DateField(null=True, verbose_name="创建时间")
    hcontent = HTMLField(verbose_name="正文")
    category = models.ForeignKey(Category, null=True, verbose_name="分类")  # 多对一  （博客--类别)
    tag = models.ManyToManyField(Tag, verbose_name="标签")  # 多对多

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
        verbose_name = "文章"
        verbose_name_plural = verbose_name

