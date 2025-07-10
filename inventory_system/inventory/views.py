from django.shortcuts import render

def home(request):
    return render(request, 'inventory/home.html')


# Create your views here.
