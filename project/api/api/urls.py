from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from apiapp import views

router = routers.DefaultRouter()
router.register('UsedCar', views.UsedCar) #views.py에서 만들었던 UsedCar클래스를 연동시킵니다. 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
