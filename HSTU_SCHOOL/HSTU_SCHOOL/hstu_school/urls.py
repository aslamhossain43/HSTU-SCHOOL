from django.conf.urls import url
from django.urls import path, include

from hstu_school import views

urlpatterns = [
    url('', views.home,name='home'),


]
