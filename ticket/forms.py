from django import forms
from .models import TicketSubmission

class TicketSubmissionForm(forms.ModelForm):
    class Meta:
        model = TicketSubmission
        fields = ['nama', 'kontak', 'tipe', 'tf']
