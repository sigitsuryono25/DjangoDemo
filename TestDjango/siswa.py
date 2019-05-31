from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from TestDjango.kelas import getDaftarKelas
from TestDjango.models import Student


@login_required(login_url='/index/')
class Siswa():
    def daftarSiswa(self):
        result = Student.objects.raw(
            "SELECT * FROM testdjango_student LEFT JOIN testdjango_kelas ON testdjango_student.kelas=testdjango_kelas.class_id ORDER BY testdjango_student.student_id ASC")
        return render(self, "daftar-siswa.html", {'res': result})

    def hapusSiswa(self):
        student_id = self.GET['student-id']
        Student.objects.filter(student_id=student_id).delete()
        return redirect(self.daftarSiswa)

    def form_tambah_siswa(self):
        global lastNim
        last = self.getNim
        kelas = getDaftarKelas()

        for r in last:
            lastNim = r.student_id
        split = lastNim.split(".")
        angkatan = split[0]
        jurusan = split[1]
        urutan = split[2]
        nextUrutan = int(urutan) + 1
        return render(self, "form-tambah-siswa.html",
                      {"last": str(nextUrutan).zfill(4), "jurusan": jurusan, "angkatan": angkatan, "kelas": kelas})

    def getNim(self):
        result = Student.objects.raw("SELECT * FROM testdjango_student ORDER BY student_id DESC LIMIT 1")
        return result

    # def getDaftarKelas():
    #     result = Kelas.objects.raw("SELECT * FROM testdjango_kelas")
    #     return result

    def insertSiswa(self):
        id = self.POST['student_id']
        fname = self.POST['first_name']
        lname = self.POST['last_name']
        pob = self.POST['pob']
        tanggal_lahir = self.POST['tanggal_lahir']
        student_email = self.POST['student_email']
        student_phone = self.POST['student_phone']
        kelas = self.POST['kelas']
        student = Student(student_id=id, first_name=fname, last_name=lname, place_of_birth=pob,
                          date_of_birth=tanggal_lahir,
                          email=student_email, phone_number=student_phone, kelas=kelas)
        student.save()
        return redirect(self.daftarSiswa)
