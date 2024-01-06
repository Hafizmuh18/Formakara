from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class TicketSubmission(models.Model):
    kode=models.CharField(max_length=255, default="None")
    nama = models.CharField(max_length=255)
    kontak = models.CharField(max_length=255)
    tipe = models.CharField(max_length=50, choices=[('Seminar', 'Seminar'), ('Try Out', 'Try Out'), ('Bundle 1', 'Bundling 1'), ('Bundle 2', 'Bundling 2')])
    nama2 =  models.CharField(max_length=255)
    kontak2 = models.CharField(max_length=255)
    tf = models.ImageField(upload_to='static/proof_image/')
    used = models.CharField(max_length=10, default="No")
    note = models.TextField(default="-")
    status = models.TextField(default="Tunggu Konfirmasi")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nama  # Display the name in the admin interface or elsewhere
