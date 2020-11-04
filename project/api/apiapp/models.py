from django.db import models

class UsedCar(models.Model):
    accident_history = models.CharField(max_length = 20, blank=True, default ='')
    repair_history = models.TextField(blank=True, default ='')
    manufacturer = models.CharField(max_length = 20, blank=True,default ='')

    class Meta:
        verbose_name_plural = 'UsedCar'

    def __str__(self):
        return self.id

#전반적으로 apps의 model과 똑같습니다.
