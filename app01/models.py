from django.db import models

# Create your models here.


class ClassInfo(models.Model):
    name=models.CharField(max_length=32)
    classes=models.CharField(max_length=32)
    gender=models.CharField(max_length=8)

