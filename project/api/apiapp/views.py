from django.shortcuts import render
from .models import UsedCar
from django.views import View, generic
from rest_framework import viewsets
from .serializers import UsedCarSerializer
# Create your views here.

class UsedCar(viewsets.ModelViewSet): #rest_framework에서 임포트한 viewsets의 ModelViewSet을 상속/연동합니다.
                                      #ModelViewSet은 서버를 실행하면 화면에 데이터를 출력해서 Read할 수 있게 해줍니다.
    queryset = UsedCar.objects.all()
    serializer_class =  UsedCarSerializer
