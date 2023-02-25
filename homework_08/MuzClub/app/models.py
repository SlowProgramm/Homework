from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=24)
    color = models.CharField(verbose_name='color code', max_length=9, null=True, blank=True)
# color - это цвет, которым будет оформлена страница DetailView


class Author(models.Model):
    username = models.CharField(verbose_name='username', max_length=64)


class Songs(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    rating = models.CharField(verbose_name='rating',  null=True, blank=True, max_length=2)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)


