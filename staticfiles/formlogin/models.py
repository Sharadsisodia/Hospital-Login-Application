from django.db import models

# Create your models here.

class patient(models.Model):
    p_Firstname=models.CharField(max_length=50)
    p_Lastname=models.CharField(max_length=50)
    p_Picture=models.ImageField(upload_to='images/')
    p_Username=models.CharField(max_length=20)
    p_EmailId=models.CharField(max_length=50)
    p_Password=models.CharField(max_length=20)
    p_AddressLi=models.TextField()
    p_City=models.CharField(max_length=25)
    p_State=models.CharField(max_length=25)
    p_Pincode=models.IntegerField()

class doctor(models.Model):
    d_Firstname=models.CharField(max_length=50)
    d_Lastname=models.CharField(max_length=50)
    d_Picture=models.FileField(upload_to='images/')
    d_Username=models.CharField(max_length=20)
    d_EmailId=models.CharField(max_length=50)
    d_Password=models.CharField(max_length=20)
    d_AddressLi=models.TextField()
    d_City=models.CharField(max_length=25)
    d_State=models.CharField(max_length=25)
    d_Pincode=models.IntegerField()
