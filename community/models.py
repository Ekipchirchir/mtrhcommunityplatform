from django.db import models

# Create your models here.

class Doctors(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    pf_number=models.IntegerField()
    email = models.EmailField(max_length=254)
    date_time= models.DateTimeField()
    phone_number = models.IntegerField()

class Nurses(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    pf_number=models.IntegerField()
    email = models.EmailField(max_length=254)
    date_time=models.DateTimeField()
    phone_number=models.IntegerField()

class SupportStaff(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    pf_number=models.IntegerField()
    email = models.EmailField(max_length=254)
    date_time=models.DateTimeField()
    phone_number=models.IntegerField()

class AlliedHealthProfessionals(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    pf_number=models.IntegerField()
    email = models.EmailField(max_length=254)
    date_time=models.DateTimeField()
    phone_number=models.IntegerField()
