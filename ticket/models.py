import os
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

def upload_to(instance, filename):
    now = timezone.now()
    date_folder = now.strftime('%Y/%m/%d')
    return os.path.join('images', date_folder, filename)

class TicketSubmission(models.Model):
    kode=models.CharField(max_length=255, default="None")
    username = models.CharField(max_length=255, default="None")
    username2 = models.CharField(max_length=255, default="None")
    nama = models.CharField(max_length=255)
    kontak = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    asal = models.CharField(max_length=255)
    tipe = models.CharField(max_length=50, choices=[('Seminar', 'Seminar'), ('Try Out', 'Try Out'), ('Bundle 1', 'Bundling 1'), ('Bundle 2', 'Bundling 2')])
    nama2 =  models.CharField(max_length=255)
    kontak2 = models.CharField(max_length=255)
    email2 = models.CharField(max_length=255)
    asal2 = models.CharField(max_length=255)
    tf = models.ImageField(upload_to=upload_to)
    used = models.CharField(max_length=10, default="No")
    note = models.TextField(default="-")
    status = models.TextField(default="Tunggu Konfirmasi")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama  # Display the name in the admin interface or elsewhere
