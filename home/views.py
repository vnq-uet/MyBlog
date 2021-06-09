from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, 'pages/home.html')

def get_contact(request):
    return render(request, 'pages/contact.html')

def register(request):
    pass