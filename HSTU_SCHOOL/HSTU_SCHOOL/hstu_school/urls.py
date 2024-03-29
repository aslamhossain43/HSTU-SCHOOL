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

    # for news
    path('addNews/', views.addNews, name='addNews'),
    path('editNews/<id>', views.requestForUpdateNews, name='requestForUpdateNews'),
    path('updateNews/<id>', views.updateNews, name='updateNews'),
    path('deleteNews/<id>', views.deleteNews, name='deleteNews'),
   # for news
    path('showEmailForm/',views.showEmailForm,name='showEmailForm'),
    path('addEmail/', views.addEmail, name='addEmail'),
    path('sendEmail/', views.sendEmail, name='sendEmail'),
    # for fblink
    path('addFblink/',views.addFblink,name='addFblink'),
    # for fblink
    path('addTwitterlink/',views.addTwitterlink,name='addTwitterlink'),
    # for contact
    path('addContact/',views.addContact,name='addContact'),
    # for carousel
    path('addCarousel/',views.addCarousel,name='addCarousel'),
    # for home
    path('addHome/',views.addHome,name='addHome'),
    # for history
    path('addHistory/',views.addHistory,name='addHistory'),
    # for about
    path('addAbout/', views.addAbout, name='addAbout'),

]

if settings.DEBUG: # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)