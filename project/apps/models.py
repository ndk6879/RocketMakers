from django.db import models

class UsedCar(models.Model):
    accident_history = models.CharField(max_length = 20, blank=True, default ='')
    repair_history = models.TextField(blank=True, default ='')
    manufacturer = models.CharField(max_length = 20, blank=True,default ='')

    class Meta:
        verbose_name_plural = 'UsedCar'

    def __str__(self):
        # admin에서 저장하면 object말고 return값인 id가 출력됩니다.
        # 모델 필드들을 보고 데이터들을 구분하기는 어려워서 id값을 return했습니다. 
        return self.id
