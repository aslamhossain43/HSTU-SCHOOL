from django.contrib import admin

# Register your models here.
from hstu_school.models import TeacherList, StaffList, Notice, Event, News, EmailHost, Fblink, Twitterlink, Contact, \
    Carousel, Home, History, About

admin.site.register(TeacherList)
admin.site.register(StaffList)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(EmailHost)
admin.site.register(Fblink)
admin.site.register(Twitterlink)
admin.site.register(Contact)
admin.site.register(Carousel)
admin.site.register(Home)
admin.site.register(History)
admin.site.register(About)





