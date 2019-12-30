# coding:utf-8

from django.conf.urls import url
from django.contrib import admin

from student.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]