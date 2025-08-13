from django.db import models


# Create your models here.
class Registration(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   address = models.TextField()


class RegistrationForm(models.Model):
   username = models.CharField(max_length=100)
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=100)