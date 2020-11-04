from django import forms
from django.db import models
from .models import UsedCar
class UsedCarForm(forms.ModelForm):

    class Meta:
        model = UsedCar #모델 UsedCar을 받아옵니다.
        fields = ['accident_history', 'repair_history', 'manufacturer'] #모델 UsedCar의 필드 중에서 사용할 필드들을 받아옵니다.
