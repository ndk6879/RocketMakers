from django.urls import path, re_path
from django.conf.urls import url
from apps import views
import sys
import io
import cgi
from .forms import *

app_name = 'UsedCar'
urlpatterns = [
    path('', views.main, name = 'main'), #메인페이지를 위한 url
    path('survey', views.survey, name = 'survey'), #메인페이지에서 survey를 누르면 가는 url
    ]
