# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect

from TestDjango.models import Student


def index(req):
    # stu = StudentForms()
    return render(req, "index.html", {})


def loginSiswa(req):
    id = req.POST['student-id']
    ttl = req.POST['ttl-student']
    result = Student.objects.raw(
        "SELECT * FROM testdjango_student WHERE student_id='{0}' AND date_of_birth='{1}'".format(id, ttl))
    req.session['username'] = id
    req.session['name'] = result[0].first_name + " " + result[0].last_name
    return HttpResponse()


def home(req):
    username = req.session['username']
    return render(req, 'form-tambah-siswa.html', {'username': username})


def logout(req):
    req.session.flush()
    return redirect(index)
