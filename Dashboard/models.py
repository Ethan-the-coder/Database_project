from django.db import models

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