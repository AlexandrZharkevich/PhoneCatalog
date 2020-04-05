from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=255)
    reg_date = models.DateField('registration date')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
