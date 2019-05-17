from django.conf import settings
from django.conf.urls.static import static
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
    # for teacher
    path('addTeacherList/',views.addTeacherList,name='addTeacherList'),
    path('editTeacher/<id>',views.requestForUpdateTeacherList,name='requestForUpdateTeacherList'),
    path('updateTeacherList/<id>',views.updateTeacherList,name='updateTeacher'),
    path('deleteTeacher/<id>',views.deleteTeacher,name='deleteTeacher'),

    # for staff
    path('addStaffList/',views.addStaffList,name='addStaffList'),
    path('editStaff/<id>',views.requestForUpdateStaffList,name='requestForUpdateStaffList'),
    path('updateStaffList/<id>',views.updateStaffList,name='updateStaff'),
    path('deleteStaff/<id>',views.deleteStaff,name='deleteStaff'),
    # for notice
    path('addNotice/', views.addNotice, name='addNotice'),
    path('editNotice/<id>', views.requestForUpdateNotice, name='requestForUpdateNotice'),
    path('updateNotice/<id>', views.updateNOtice, name='updateNotice'),
    path('deleteNotice/<id>', views.deleteNotice, name='deleteNotice'),

    # for event
    path('addEvent/', views.addEvent, name='addEvent'),
    path('editEvent/<id>', views.requestForUpdateEvent, name='requestForUpdateEvent'),
    path('updateEvent/<id>', views.updateEvent, name='updateEvent'),
    path('deleteEvent/<id>', views.deleteEvent, name='deleteEvent'),

]

if settings.DEBUG: # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)