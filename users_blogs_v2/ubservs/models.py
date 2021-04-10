from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.core.mail import send_mail
from users_blogs_v2.celery import app
from celery import shared_task
import smtplib
from threading import Thread




class User(AbstractUser):
    blogs_subcribe = models.ManyToManyField('Blog', blank=True,
                                   verbose_name='Подписные блоги', null=True)
    read_posts = models.ManyToManyField('Post', blank=True,
                                   verbose_name='Прочитанные новосные посты', null=True)
    
    objects = UserManager()

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
    author = models.OneToOneField(User, on_delete=models.CASCADE, 
                               verbose_name='Автор блога')
    
    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    class Meta():
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        db_table = 'blogs'
        ordering = ['-id']


# Функция обработки сигнала post_save, которая вызывается 
# внутри регистрируемой функции my_callback
@app.task
def indef_task():
    instance = Post.objects.latest('timestamp')
    users = User.objects.all()
    for el in users:
        for ele in el.blogs_subcribe.all():
            if ele.author == instance.author:
                try:
                    send_mail('Add a new post in your News', 
                              'Dear {}, user {} add a new post. See it in the /news/'.
                               format(el.username, instance.author), 
                              'from@example.com',  [f'{el.email}'], fail_silently=False)
                except Exception as e:
                    print('Letter was not send to user {} by E-mail: {}'.format(el.username, 
                                                                        el.email), e)


def my_callback(sender, **kwargs):
    indef_task.delay()  


post_save.connect(my_callback, sender=Post)
