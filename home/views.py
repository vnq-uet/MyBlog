from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect

# Create your views here.
def get_home(request):
    return render(request, 'pages/home.html')

def get_contact(request):
    return render(request, 'pages/contact.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form':form})
        
    
