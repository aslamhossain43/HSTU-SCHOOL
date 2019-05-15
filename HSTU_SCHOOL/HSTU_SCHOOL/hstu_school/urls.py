from django.urls import path

from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('history/', views.history,name='history'),
    path('about/', views.about,name='about'),
    path('teacher-list/', views.teacherlist,name='teacher-list'),
    path('staff-list/', views.stafflist,name='staff-list'),
    path('notice/', views.notice,name='notice'),
    path('event/', views.event,name='event'),
    path('news/', views.news,name='news'),
    path('manage/', views.manage,name='manage'),




]