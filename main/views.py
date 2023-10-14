from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def broadcast(request):
    return render(request, 'broadcast.html')
