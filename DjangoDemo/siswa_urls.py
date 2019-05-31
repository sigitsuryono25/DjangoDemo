from django.urls import path

from TestDjango import siswa

urlpatterns = [
    path('daftar-siswa/', siswa.Siswa.daftarSiswa),
    path('tambah-siswa/', siswa.Siswa.form_tambah_siswa),
    path('tambah-siswa-proses/', siswa.Siswa.insertSiswa),
    path('hapus-siswa/', siswa.Siswa.hapusSiswa),
]
