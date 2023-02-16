from django.db import models

class Weather(models.Model):
    prefecture = models.CharField(max_length = 10)
    weather = models.CharField(max_length = 10)
    temperature = models.IntegerField(null = True) # 既存のデータに合わせるため空値OKにした

    def __str__(self):
        return self.prefecture

    class Meta:
        verbose_name = verbose_name_plural = "WeatherInfo"