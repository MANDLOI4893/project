from distutils.command.upload import upload
from email.headerregistry import Address
from email.mime import image
from email.policy import default
from opcode import opname
from unicodedata import category
from django.db import models


# Create your models here.
class invcard(models.Model):
    code= models.CharField(max_length=30, unique=True,primary_key=True, default='')
    category= models.CharField(max_length=50, default='')
    offer= models.CharField(max_length=20, blank=True, default='')
    tag= models.CharField(max_length=10, blank=True, default='')
    price= models.IntegerField(default='')
    content= models.CharField(max_length=200, default='')
    more_info= models.TextField(max_length=300, default='')
    image= models.ImageField(upload_to= 'images/%y', default='')
    video= models.FileField(upload_to='video/%y', blank=True, default='')
    date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.code
    

class contact(models.Model):
    contact_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=40,)
    email= models.CharField(max_length=30, blank=True, default='')
    number= models.IntegerField( default='')
    address= models.CharField(max_length=100, blank=True, default='')
    desc= models.CharField(max_length=200, default='')
    

    def __str__(self):
        return self.name

class team(models.Model):
    name= models.CharField(max_length=40,)
    work= models.CharField(max_length=30, default='')
    content= models.CharField(max_length=100,  default='')
    image= models.ImageField(upload_to= 'images/%y', default='')

    def __str__(self):
        return self.name    

class faq(models.Model):
    question= models.CharField(max_length=100,)
    answer= models.CharField(max_length=300, default='')
    def __str__(self):
        return self.question             

class offer(models.Model):
    oname = models.CharField(max_length=100)
    offer1= models.ImageField(upload_to= 'images/%y', default='')
    offer2= models.ImageField(upload_to= 'images/%y', default='')    
    def __str__(self):
        return self.oname    