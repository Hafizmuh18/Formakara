from django.db import models

# Create your models here.
from django.db import models

class TicketSubmission(models.Model):
    nama = models.CharField(max_length=255)
    kontak = models.CharField(max_length=255)
    tipe = models.CharField(max_length=50, choices=[('seminar', 'Seminar'), ('to', 'Try Out'), ('bundle', 'Bundling')])
    # Assuming you want to store the uploaded image in a 'proof_of_transfer' directory within your media folder
    tf = models.ImageField(upload_to='static/proof_image/')
    used = models.CharField(max_length=10, default="No")

    def __str__(self):
        return self.nama  # Display the name in the admin interface or elsewhere
