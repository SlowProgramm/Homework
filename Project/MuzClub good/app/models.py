from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    title = models.CharField(verbose_name='title', max_length=24)
    color = models.CharField(verbose_name='color code', max_length=9, null=True, blank=True)
# color - это цвет, которым будет оформлена страница DetailView

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    username = models.CharField(verbose_name='username', max_length=64)

    def __str__(self):
        return f'{self.username}'


class Songs(models.Model):
    name = models.CharField(verbose_name='name', max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, max_length=255)
    file = models.FileField(upload_to='songs/', null=False, blank=False)


    # def __str__(self):
    #     return f'{self.name} [{self.category.title}] [{self.author.username}] [{self.rating}]'


