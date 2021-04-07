from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    blogs_suscribe = models.ManyToManyField('Blog', blank=True,
                                   verbose_name='blogs', null=True)
    read_posts = models.ManyToManyField('Post', blank=True,
                                   verbose_name='posts', null=True)
    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username


class Post(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Post id')
    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    text = models.TextField(verbose_name='Текст поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               verbose_name='Автор поста')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, 
                                     verbose_name='Дата создания поста')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'posts'
        ordering = ['-id']


class Blog(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Blog id')
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               verbose_name='Автор блога')
    posts = models.ManyToManyField(Post, blank=True,
                                   verbose_name='posts', null=True)
    
    def __unicode__(self):
        return self.id

    def __str__(self):
        return self.id

    class Meta():
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        db_table = 'blogs'
        ordering = ['-id']
