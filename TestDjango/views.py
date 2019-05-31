from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect

from TestDjango.models import Student
from TestDjango.models import Kelas


def index(req):
    # stu = StudentForms()
    return render(req, "index.html", {})


def result(req):
    id = req.POST['student_id']
    fname = req.POST['first_name']
    lname = req.POST['last_name']
    pob = req.POST['pob']
    tanggal_lahir = req.POST['tanggal_lahir']
    student_email = req.POST['student_email']
    student_phone = req.POST['student_phone']

    student = Student(student_id=id, first_name=fname, last_name=lname, place_of_birth=pob, date_of_birth=tanggal_lahir,
                      email=student_email, phone_number=student_phone)
    student.save()

    html = "<html><body>Student ID is and Date of Birth is .</body></html>"
    return HttpResponse(html)


def getStudent(req):
    result = Student.objects.raw("SELECT * FROM testdjango_student")
    return render(req, "daftar-siswa.html", {'res': result})

def getKelas(req):
    result = Kelas.objects.raw("SELECT * FROM testdjango_kelas")
    return render(req, "daftar-kelas.html", {"kelas" : result})

def process(req):
    id = req.POST['student-id']
    ttl = req.POST['ttl-student']
    result = Student.objects.raw(
        "SELECT * FROM testdjango_student WHERE student_id='{0}' AND date_of_birth='{1}'".format(id, ttl))
    req.session['username'] = id;
    return HttpResponse()

def deleteKelas(req):
    idKelas = req.GET['id-kelas']
    Kelas.objects.filter(class_id=idKelas).delete()
    return redirect(getKelas)

def home(req):
    username = req.session['username']
    return render(req, 'home.html', {'username': username})
