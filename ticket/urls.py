from django.urls import path
from .views import *

app_name = 'ticket'

urlpatterns = [
    path('', make_ticket, name='make_ticket'),
    path('submit/', submit_ticket, name='submit_ticket'),
    path('ticket/<int:ticket_id>/', show_ticket, name='show_ticket'),  # Updated URL pattern with a parameter
    path('tiket-data/admin/ybm24/', ticket_data, name='ticket_data'),
    path('mark_ticket_as_used/<int:ticket_id>/', mark_ticket_as_used, name='mark_ticket_as_used'),
    path('mark_ticket_as_not_used/<int:ticket_id>/', mark_ticket_as_not_used, name='mark_ticket_as_not_used'),
    path('delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
]