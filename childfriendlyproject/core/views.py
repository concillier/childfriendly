from django.shortcuts import render

# Create your views here.

def homepage(request): 
    return render(request, 'home.html')


def contactpage(request): 
    return render(request, 'contact.html')


def placepage(request):
    return render(request, 'place.html')
    

