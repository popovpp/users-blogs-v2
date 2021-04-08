from django.contrib import admin
from django.urls import path
from django.urls import re_path
from ubservs import views
from django.conf.urls import include
import django.contrib.auth.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include('ubservs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/profile/', views.PostList.as_view()),
]
