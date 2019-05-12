from django.conf.urls import url
from django.contrib import admin
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('hstu_school.urls'))

]
