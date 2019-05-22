import os
import random
import string

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from hstu_school.models import TeacherList, StaffList, Notice, Event, News, EmailHost, Fblink, Twitterlink, Contact, \
    Carousel, Home, History, About


def home(request):
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    home = Home.objects.filter()[:1].get()
    context = {
        'fbLinkForNav':fbLink,
        'twitterLinkForNavbar':twitterLink,
        'contact':contact,
        'carousel':carousel,
        'home':home,
    }
    return render(request, 'home.html', context)

def history(request):
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    history = History.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'history': history,

    }
    return render(request, 'history.html', context)

def about(request):
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    about = About.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'about': about,
    }
    return render(request, 'about.html', context)
def teacherlist(request):
    teacherList = TeacherList.objects.all()
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'tList': teacherList,
    }

    return render(request, 'teacher-list.html', context)
def stafflist(request):
    staffList = StaffList.objects.all()
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'sList': staffList,
    }
    return render(request,'staff-list.html',context)


def news(request):
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,

    }
    return render(request, 'news.html', context)
def manage(request):
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()

    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notices = Notice.objects.all()
    events = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contacts = Contact.objects.all()
    carousels = Carousel.objects.all()
    home = Home.objects.all()
    history = History.objects.all()
    about = About.objects.all()

    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,

        'tList': teacherList,
        'sList': staffList,
        'notice': notices,
        'event':events,
        'newss':newss,
        'email':email,
        'fblink':fblink,
        'twitterlink':twitterlink,
        'contacts':contacts,
        'carousels':carousels,
        'home': home,
        'history': history,
        'about': about,


    }
    return render(request, 'manage.html', context)
def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
# for teacher
def addTeacherList(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         job = request.POST.get('job')
         contact = request.POST.get('contact')
         photo_code = randomword(20)
         teacherList = TeacherList(name = name,job = job,contact = contact,photo_code = photo_code)
         teacherList.save()
         photo = request.FILES['photo']
         fs = FileSystemStorage()
         # logger.info('from addTeacher()')
         fs.save(photo_code + '.jpg', photo)
    return redirect('/manage')
def requestForUpdateTeacherList(request,id):
    updateTeacher = 'update'

    teacherlist = TeacherList.objects.get(id = id)
    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notice = Notice.objects.all()
    event = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contact = Contact.objects.all()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'updateTeacher': updateTeacher,
        'teacher':teacherlist,
        'tList': teacherList,
        'sList': staffList,
        'notice': notice,
        'event': event,
        'newss':newss,
        'email':email,
        'fblink':fblink,
        'twitterlink':twitterlink,
        'contact':contact,
        'carousel':carousel,



    }
    return render(request, 'manage.html', context)

def updateTeacherList(request,id):

    if request.method == 'POST':
         teacherlist = TeacherList.objects.get(id = id)
         teacherlist.name = request.POST.get('name')
         teacherlist.job = request.POST.get('job')
         teacherlist.contact = request.POST.get('contact')
         os.remove('images/' + teacherlist.photo_code + '.jpg')
         teacherlist.photo_code = randomword(20)
         photo = request.FILES['photo']
         fs = FileSystemStorage()
         # logger.info('from addTeacher()')
         fs.save(teacherlist.photo_code + '.jpg', photo)
         teacherlist.save()

    return redirect('/manage')

def deleteTeacher(request,id):
     teacher=TeacherList.objects.get(id = id)
     os.remove('images/' + teacher.photo_code + '.jpg')
     teacher.delete()
     return redirect('/manage')
# for staff
def addStaffList(request):
    if request.method == 'POST':
         name = request.POST.get('name')
         job = request.POST.get('job')
         contact = request.POST.get('contact')
         photo_code = randomword(20)
         staffList = StaffList(name = name,job = job,contact = contact,photo_code = photo_code)
         staffList.save()
         photo = request.FILES['photo']
         fs = FileSystemStorage()
         # logger.info('from addTeacher()')
         fs.save(photo_code + '.jpg', photo)
    return redirect('/manage')
def requestForUpdateStaffList(request,id):
    updateStaff = 'update'

    stafflist = StaffList.objects.get(id = id)
    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notices = Notice.objects.all()
    events = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contact = Contact.objects.all()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'updateStaff': updateStaff,
        'staff':stafflist,
        'tList': teacherList,
        'sList': staffList,
        'notice': notices,
        'event': events,
        'newss':newss,
        'email': email,
        'fblink': fblink,
        'twitterlink': twitterlink,
        'contact':contact,
        'carousel':carousel,
    }
    return render(request,'manage.html',context)

def updateStaffList(request,id):

    if request.method == 'POST':
         stafflist = StaffList.objects.get(id = id)
         stafflist.name = request.POST.get('name')
         stafflist.job = request.POST.get('job')
         stafflist.contact = request.POST.get('contact')
         os.remove('images/' + stafflist.photo_code + '.jpg')
         stafflist.photo_code = randomword(20)
         photo = request.FILES['photo']
         fs = FileSystemStorage()
         # logger.info('from addTeacher()')
         fs.save(stafflist.photo_code + '.jpg', photo)
         stafflist.save()

    return redirect('/manage')

def deleteStaff(request,id):
     staff = StaffList.objects.get(id = id)
     os.remove('images/' + staff.photo_code + '.jpg')
     staff.delete()
     return redirect('/manage')




# -----------------------for notice-----------------------------------------------------------
def notice(request):
    notices = Notice.objects.all()
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'notice': notices,
    }
    return render(request, 'notice.html', context)

def addNotice(request):
    if request.method == 'POST':
         notice_heading = request.POST.get('notice_heading')
         notice_details = request.POST.get('notice_details')
         notices=Notice(notice_heading = notice_heading,notice_details = notice_details)
         notices.save()
    return redirect('/manage')
def requestForUpdateNotice(request,id):
    updateNotice = 'update'

    notice = Notice.objects.get(id = id)
    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notices = Notice.objects.all()
    events = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contact = Contact.objects.all()
    carousel = Carousel.objects.filter()[:1].get()

    context = {
        'updateNotice': updateNotice,
        'staff':stafflist,
        'tList': teacherList,
        'sList': staffList,
        'notice': notices,
        'notic': notice,
        'event': events,
        'newss':newss,
        'email': email,
        'fblink': fblink,
        'twitterlink': twitterlink,
        'contact':contact,
        'carousel':carousel,


    }
    return render(request,'manage.html',context)

def updateNOtice(request,id):

    if request.method == 'POST':
         notice = Notice.objects.get(id = id)
         notice.notice_heading = request.POST.get('notice_heading')
         notice.notice_details = request.POST.get('notice_details')
         notice.save()
    return redirect('/manage')

def deleteNotice(request,id):
      notice = Notice.objects.get(id = id)
      notice.delete()
      return redirect('/manage')
# -----------------------for notice-----------------------------------------------------------
def event(request):
    events = Event.objects.all()
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'event':events,
    }
    return render(request, 'event.html', context)
def addEvent(request):
    if request.method == 'POST':
         event_heading = request.POST.get('event_heading')
         event_location = request.POST.get('event_location')
         event_details = request.POST.get('event_details')
         events=Event(event_heading = event_heading,event_location = event_location,event_details = event_details)
         events.save()
    return redirect('/manage')
def requestForUpdateEvent(request,id):
    updateEvent = 'update'

    event = Event.objects.get(id = id)
    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notices = Notice.objects.all()
    events = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contact = Contact.objects.all()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'updateEvent': updateEvent,
        'staff':stafflist,
        'tList': teacherList,
        'sList': staffList,
        'notice': notices,
        'notic': notice,
        'event':events,
        'even':event,
        'newss':newss,
        'email': email,
        'fblink': fblink,
        'twitterlink': twitterlink,
        'contact':contact,
        'carousel':carousel,


    }
    return render(request,'manage.html',context)

def updateEvent(request,id):

    if request.method == 'POST':
         event = Event.objects.get(id = id)
         event.event_heading = request.POST.get('event_heading')
         event.event_location = request.POST.get('event_location')
         event.event_details = request.POST.get('event_details')
         event.save()
    return redirect('/manage')

def deleteEvent(request,id):
      event = Event.objects.get(id = id)
      event.delete()
      return redirect('/manage')
# -----------------------for news-----------------------------------------------------------
def news(request):
    newss = News.objects.all()
    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    contact = Contact.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'contact':contact,
        'carousel':carousel,
        'newss':newss,
    }
    return render(request, 'news.html', context)
def addNews(request):
    if request.method == 'POST':
         news_heading = request.POST.get('news_heading')
         news_details = request.POST.get('news_details')
         news = News(news_heading = news_heading,news_details = news_details)
         news.save()
    return redirect('/manage')
def requestForUpdateNews(request,id):
    updateNews = 'update'

    news = News.objects.get(id = id)
    teacherList = TeacherList.objects.all()
    staffList = StaffList.objects.all()
    notices = Notice.objects.all()
    events = Event.objects.all()
    newss = News.objects.all()
    email = EmailHost.objects.all()
    fblink = Fblink.objects.all()
    twitterlink = Twitterlink.objects.all()
    contact = Contact.objects.all()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'updateNews': updateNews,
        'staff':stafflist,
        'tList': teacherList,
        'sList': staffList,
        'notice': notices,
        'notic': notice,
        'event':events,
        'even':event,
        'news':news,
        'newss':newss,
        'email': email,
        'fblink': fblink,
        'twitterlink': twitterlink,
        'contact':contact,
        'carousel':carousel,


    }
    return render(request,'manage.html',context)

def updateNews(request,id):

    if request.method == 'POST':
         news = News.objects.get(id = id)
         news.news_heading = request.POST.get('news_heading')
         news.news_details = request.POST.get('news_details')
         news.save()
    return redirect('/manage')

def deleteNews(request,id):
      news = News.objects.get(id = id)
      news.delete()
      return redirect('/manage')


# for email
def showEmailForm(request):
    context = {}
    return render(request,'email.html',context)

def addEmail(request):
    if request.method == 'POST':
        emails = EmailHost.objects.all()
        emails.delete()
        user = request.POST.get('user')
        password = request.POST.get('password')
        email = EmailHost(user = user, password = password)
        email.save()
    return redirect('/manage')
def sendEmail(request):

    successMsg = 'Email has been sent successfully !!!'

    fbLink = Fblink.objects.filter()[:1].get()
    twitterLink = Twitterlink.objects.filter()[:1].get()
    carousel = Carousel.objects.filter()[:1].get()
    context = {
        'fbLinkForNav': fbLink,
        'twitterLinkForNavbar': twitterLink,
        'carousel':carousel,
        'emailSuccessMsg': successMsg,
    }
    if request.method == 'POST':
        hostEmail = EmailHost.objects.all().first()
        settings.EMAIL_HOST_USER = hostEmail.user
        settings.EMAIL_HOST_PASSWORD = hostEmail.password
        #3 email id used ,,host,from,to
        #your host email must be less secure
        #https://myaccount.google.com/lesssecureapps?pli=1
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email_from = request.POST.get('from')
        recipient_list = [hostEmail.user]

        send_mail(subject, message, email_from, recipient_list)

    return render(request,'email.html',context)

def addFblink(request):
    if request.method == 'POST':
        fblinks = Fblink.objects.all()
        fblinks.delete()
        link = request.POST.get('fblink')
        fblink = Fblink(fblink = link)
        fblink.save()
    return redirect('/manage')


def addTwitterlink(request):
    if request.method == 'POST':
        twitterlinks = Twitterlink.objects.all()
        twitterlinks.delete()
        link = request.POST.get('twitterlink')
        twitterlink = Twitterlink(twitterlink = link)
        twitterlink.save()
    return redirect('/manage')

def addContact(request):
    if request.method == 'POST':
        contacts = Contact.objects.all()
        contacts.delete()
        info_line = request.POST.get('infoline')
        fax = request.POST.get('fax')
        email = request.POST.get('email')
        contact = Contact(info_line = info_line,fax = fax,email = email)
        contact.save()
    return redirect('/manage')


# for carousel
def addCarousel(request):
    if request.method == 'POST':
         carousels = Carousel.objects.filter()[:1].get()
         os.remove('images/'+carousels.pic1+'.jpg')
         os.remove('images/' + carousels.pic2 + '.jpg')
         os.remove('images/' + carousels.pic3 + '.jpg')

         carousels.delete()
         pic1 = randomword(20)
         pic2 = randomword(20)
         pic3 = randomword(20)
         carousel = Carousel(pic1 = pic1,pic2 = pic2,pic3 = pic3)
         carousel.save()
         photo1 = request.FILES['photo1']
         photo2 = request.FILES['photo2']
         photo3 = request.FILES['photo3']

         fs = FileSystemStorage()
         fs.save(pic1 + '.jpg', photo1)
         fs.save(pic2 + '.jpg', photo2)
         fs.save(pic3 + '.jpg', photo3)

    return redirect('/manage')

# for Home
def addHome(request):
    if request.method == 'POST':
         homes = Home.objects.filter()[:1].get()
         os.remove('images/'+homes.home_pic+'.jpg')

         homes.delete()
         home_pic = randomword(20)
         home_text = request.POST.get('home_text')

         home = Home(home_pic = home_pic,home_text = home_text)
         home.save()
         photo = request.FILES['home_pic']

         fs = FileSystemStorage()
         fs.save(home_pic + '.jpg', photo)

    return redirect('/manage')

# for History
def addHistory(request):
    if request.method == 'POST':
         histories = History.objects.filter()[:1].get()
         histories.delete()
         history_text = request.POST.get('history_text')

         history = History(history_text = history_text)
         history.save()
    return redirect('/manage')
# for About
def addAbout(request):
    if request.method == 'POST':
         abouts = About.objects.filter()[:1].get()
         abouts.delete()
         about_text = request.POST.get('about_text')

         about = About(about_text = about_text)
         about.save()
    return redirect('/manage')



