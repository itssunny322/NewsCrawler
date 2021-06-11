from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth
from django.conf.urls import url

urlpatterns = [
    path("",home,name="home"),
    path("search/",search,name="search"),


]