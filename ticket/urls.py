from django.urls import path, re_path
from .views import *

app_name = 'ticket'

urlpatterns = [
    path('', make_ticket, name='make_ticket'),
    path('submit/', submit_ticket, name='submit_ticket'),
    path('ticket/<str:ticket_kode>/', show_ticket, name='show_ticket'),  # Updated URL pattern with a parameter
    path('ybm24/ticket-data/', ticket_data, name='ticket_data'),
    path('mark_ticket_as_used/<int:ticket_id>/', mark_ticket_as_used, name='mark_ticket_as_used'),
    path('mark_ticket_as_not_used/<int:ticket_id>/', mark_ticket_as_not_used, name='mark_ticket_as_not_used'),
    path('set_payed/<int:ticket_id>/', set_payed, name='set_payed'),
    path('set_unpayed/<int:ticket_id>/', set_unpayed, name='set_unpayed'),
    path('delete/<int:ticket_id>/', delete_ticket, name='delete_ticket'),
    re_path(r'^.*$', custom_404, name='custom_404'),
]