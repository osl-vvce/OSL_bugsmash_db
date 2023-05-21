from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    email = models.EmailField()
    salary = models.BigIntegerField(default=0)
    