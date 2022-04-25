from datetime import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField
from django.urls import reverse


class art(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Content')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time_create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Famous Art'
        verbose_name_plural = 'Famous Art'
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
        ordering = ['id']


class museum(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Content')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Photo')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time_create')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Famous Museum'
        verbose_name_plural = 'Famous Museum'
        ordering = ['time_create', 'title']

class Registration(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=255)
    mather_name = models.CharField(max_length=15)
    father_name = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=10)


    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрация'




