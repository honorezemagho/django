from django.urls import path
from .import views 

urlpatterns = [
    path('clients', views.index, name='clients'),
    path('clients/<slug:client_slug>', views.show_clients, name='client-details')
]
