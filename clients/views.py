from django.shortcuts import render

# Create your views here.

def index(request):
    clients = [
        {'name': 'Mika Albry'},
        {'name': 'Tamka Alfred'}
    ];
    return render(request,'clients/index.html', {'show_clients': False,'clients': clients})