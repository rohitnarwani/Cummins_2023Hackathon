from django.db import models

# Create your models here.
class OfficeHours(models.Model):
    username=models.CharField(max_length=100)
    starttime=models.TimeField()
    endtime=models.TimeField()
    def __str__(self):
        return self.brand_name
