from statistics import mode
from django.db import models

# Create your models here.
class subjects(models.Model):
    id = models.AutoField(primary_key=True)
    subcode = models.CharField(max_length=10)
    regulation = models.CharField(max_length=5) 
    dept = models.CharField(max_length=45)
    subject_name = models.CharField(max_length=80)
    credits = models.CharField(max_length=2)
    sem = models.CharField(max_length=1)