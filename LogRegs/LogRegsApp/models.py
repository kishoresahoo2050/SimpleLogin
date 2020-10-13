from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    num   = models.BigIntegerField()
    password = models.CharField(max_length = 50)
    def __str__(self):
         return self.name
 
  