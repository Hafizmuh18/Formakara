from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import TicketSubmission
from django.db.models import Q
import random
import string

def custom_404(request, *args, **kwargs):
    return render(request, '404.html', status=404)

def generate_random_string(length=4):
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Create your views here.
def make_ticket(request):
    context = {}
    return render(request, 'main.html', context)

def submit_ticket(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        kontak = request.POST['kontak']
        tipe = request.POST['tipe']
        nama2 = request.POST['nama2']
        kontak2 = request.POST['kontak2']
        if tipe != "Bundle 2":
            nama2 = ""
            kontak2= ""
        note = request.POST['note']
        if note == "":
            note = "-"

        # Assuming you want to store the uploaded image in a 'proof_of_transfer' directory within your media folder
        tf = request.FILES['tf']

        # Create TicketSubmission object and save to the database
        ticket_submission = TicketSubmission(
            nama=nama,
            kontak=kontak,
            tipe=tipe,
            nama2=nama2,
            kontak2=kontak2,
            tf=tf,
            note=note
        )
        ticket_submission.save()
        kode = "YBM-"+str(generate_random_string())+str(ticket_submission.pk)
        ticket_submission.kode = kode
        ticket_submission.save()

        # Redirect to the 'show_ticket' view with the ticket ID as a parameter
        return redirect('ticket:show_ticket', ticket_kode=ticket_submission.kode)
    else:
        return render(request, '404.html')

def show_ticket(request, ticket_kode):
    # Retrieve the TicketSubmission object based on the ticket_id
    ticket_submission = TicketSubmission.objects.get(kode=ticket_kode)
    return render(request, 'submit.html', {'ticket': ticket_submission})

def mark_ticket_as_used(request, ticket_id):
    ticket = TicketSubmission.objects.get(pk=ticket_id)
    ticket.used = "Yes"
    ticket.save()
    return redirect('ticket:ticket_data')

def mark_ticket_as_not_used(request, ticket_id):
    ticket = TicketSubmission.objects.get(pk=ticket_id)
    ticket.used = "No"
    ticket.save()
    return redirect('ticket:ticket_data')

def set_payed(request, ticket_id):
    ticket = TicketSubmission.objects.get(pk=ticket_id)
    ticket.status = "Sudah Dibayar"
    ticket.save()
    return redirect('ticket:ticket_data')

def set_unpayed(request, ticket_id):
    ticket = TicketSubmission.objects.get(pk=ticket_id)
    ticket.status = "Tunggu Konfirmasi"
    ticket.save()
    return redirect('ticket:ticket_data')

def ticket_data(request):
    query = request.GET.get('q')
    
    if query:
        tickets = TicketSubmission.objects.filter(Q(nama__icontains=query) | Q(kode__icontains=query) | Q(tipe__icontains=query) | Q(used__icontains=query))
    else:
        query = ''
        tickets = TicketSubmission.objects.all()

    return render(request, 'admin.html', {'tickets': tickets, 'query': query})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(TicketSubmission, pk=ticket_id)
    ticket.delete()
    return redirect('ticket:ticket_data')