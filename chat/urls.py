from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name='index'),
    path("chat/home/", views.home, name='home'),
    path("chat/createroom/", views.createroom, name='createroom'),
    path("chat/joinroom/", views.joinroom, name='joinroom'),
    path("chat/returnrooms/", views.returnrooms, name='returnrooms'),
    path("chat/storemessages/", views.storemessages, name='storemessages'),
    path("chat/returnmessages/", views.returnmessages, name='returnmessages')
]