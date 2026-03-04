from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# New students model
class Student(models.Model):
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    date = models.DateField(null=True)
    name = models.CharField(max_length=20)
    course =models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=6,null=True)
    email = models.EmailField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name

# Exam model
class Exam(models.Model):
    name = models.CharField(max_length=20)
    exam_code = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name

# Payment model
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField()
    checkout_request_id = models.CharField(max_length=100,blank=True)
    status = models.CharField(default='Pending',max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)