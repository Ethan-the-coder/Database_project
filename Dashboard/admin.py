from django.contrib import admin

from Dashboard.models import Student
from Dashboard.models import Exam
# Register your models here.
admin.site.register(Student)
admin.site.register(Exam)