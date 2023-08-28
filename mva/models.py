from django.db import models

class membership(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  Monthly_fee = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)