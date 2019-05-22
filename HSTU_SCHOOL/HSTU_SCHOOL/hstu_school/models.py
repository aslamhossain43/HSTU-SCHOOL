import datetime

from AptUrl.Helpers import _
from django.db import models

class TeacherList(models.Model):
    name=models.CharField(max_length=50)
    job=models.CharField(max_length=150)
    contact=models.CharField(max_length=150)
    photo_code=models.CharField(max_length=20)
class StaffList(models.Model):
    name=models.CharField(max_length=50)
    job=models.CharField(max_length=150)
    contact=models.CharField(max_length=150)
    photo_code=models.CharField(max_length=20)
class Notice(models.Model):
    notice_time = models.TimeField()
    notice_time = datetime.datetime.now().time()
    notice_date = models.DateField()
    notice_date = datetime.datetime.now().date()
    notice_heading = models.CharField(max_length=150)
    notice_details = models.TextField(max_length=4000, null=True, blank=True)

class Event(models.Model):
        event_time = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)
        event_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
        event_heading = models.CharField(max_length=150)
        event_location = models.CharField(max_length=100)
        event_details = models.TextField(max_length=4000, null=True, blank=True)


class News(models.Model):
    news_time = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)
    news_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    news_heading = models.CharField(max_length=150)
    news_details = models.TextField(max_length=4000, null=True, blank=True)



class EmailHost(models.Model):
    user = models.CharField(max_length=150)
    password = models.CharField(max_length=150)


class Fblink(models.Model):
      fblink_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
      fblink = models.CharField(max_length=2000)


class Twitterlink(models.Model):
    twitterlink_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    twitterlink = models.CharField(max_length=2000)
class Contact(models.Model):
    contact_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    info_line = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Carousel(models.Model):
    carousel_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    pic1 = models.CharField(max_length=20)
    pic2 = models.CharField(max_length=20)
    pic3 = models.CharField(max_length=20)

class Home(models.Model):
    home_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    home_pic = models.CharField(max_length=20)
    home_text = models.CharField(max_length=4000)
class History(models.Model):
    history_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    history_text = models.CharField(max_length=4000)
class About(models.Model):
    about_date = models.DateField(_(u"Conversation Date"), auto_now_add=True, blank=True)
    about_text = models.CharField(max_length=4000)





