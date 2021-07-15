from django.shortcuts import render

# Create your views here.

def index(request):
    clients = [
        {'name': 'Mika Albry', 'phone': '+33 11457896','slug': 'client-1'},
        {'name': 'Tamka Alfred', 'phone': '+237 654789542', 'slug': 'client-2'}
    ];
    return render(request,'clients/index.html', {'show_clients': False,'clients': clients})

def show_clients(request, client_slug):
    client = {
        'name': 'Fred Lambert',
        'phone': '+33 457894867',
        'email': 'fredlamb02@gmail.com',
        'location': 'Paris, France'
    }
    return render(request,'clients/client.html', {'client': client})