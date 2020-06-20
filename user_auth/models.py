from django.db import models

# Create your models here.
class Testtaker(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    date_of_birth = models.DateField(null=True)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=20, choices=GENDERS)
    email_verified = models.BooleanField(default=False)

class Testsetter(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    date_of_birth = models.DateField(null=True)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=20, choices=GENDERS)
    email_verified = models.BooleanField(default=False)
    organisation = models.CharField(max_length=30, null=True)

class Testadmin(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    date_of_birth = models.DateField(null=True)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=20, choices=GENDERS)
    email_verified = models.BooleanField(default=False)
    organisation = models.CharField(max_length=30,null=True)