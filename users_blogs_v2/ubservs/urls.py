from django.contrib import admin
from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^post_create/', views.PostCreate.as_view()),
    re_path(r'^post_list/', views.PostList.as_view()),
#    re_path(r'^news/', views.NewsList.as_view()),
#    re_path(r'^newss/(?P<idPost>\d+)/', views.NewsList.post_red),
    re_path(r'^subscriptions/', views.ScrView.as_view()),
    re_path(r'^$', views.StartView.as_view()),
]

