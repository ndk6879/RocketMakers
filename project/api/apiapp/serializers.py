from .models import UsedCar
from rest_framework import serializers

class UsedCarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UsedCar #통신할 모델(models.py의 UsedCar)
        fields = ('accident_history','repair_history','manufacturer') #통신할 모델의 필드
