from datetime import datetime

from django.db import models

# Create your models here.
from django.forms import ModelForm


class Student(models.Model):
    student_id  = models.CharField(max_length=100, default="STUDENT_0001")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=20)
    date_of_birth = models.DateField(default="1990-01-01")
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)

class Kelas(models.Model):
    class_id = models.CharField(max_length=100, default="KELAS_0001")
    class_name = models.CharField(max_length=100)

class Dosen(models.Model):
    dosen_id = models.CharField(max_length=100, default="DOSEN_0001")
    nama_dosen= models.CharField(max_length=100, null=False)
    tempat_lahir = models.CharField(max_length=140, default='')
    tanggal_lahir = models.DateField(default="1990-01-01")
    alamat = models.TextField(null=False)
    telepon = models.CharField(max_length=16)

class StudentForms(ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'first_name', 'last_name', 'place_of_birth', 'email', 'phone_number']

