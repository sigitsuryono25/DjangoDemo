from django.urls import path

from TestDjango import kelas

urlpatterns = [
    path('daftar-kelas/', kelas.getKelas),
    path('hapus-kelas/', kelas.deleteKelas),
]
