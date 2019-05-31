from django.shortcuts import render, redirect

from TestDjango.models import Kelas


def getKelas(req):
    result = Kelas.objects.raw("SELECT * FROM testdjango_kelas")
    return render(req, "daftar-kelas.html", {"kelas": result})


def getDaftarKelas():
    result = Kelas.objects.raw("SELECT * FROM testdjango_kelas")
    return result


def deleteKelas(req):
    idKelas = req.GET['id-kelas']
    Kelas.objects.filter(class_id=idKelas).delete()
    return redirect(getKelas)
