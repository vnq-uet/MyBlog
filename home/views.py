from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from blog.models import Post

# Create your views here.
def get_home(request):
    posts = Post.objects.all()
    return render(request, 'pages/home.html', {'posts_size':len(posts)})

def get_contact(request):
    posts = Post.objects.all()
    return render(request, 'pages/contact.html', {'posts_size':len(posts)})

def get_skill(request):
    posts = Post.objects.all()
    return render(request, 'pages/skill.html', {'posts_size':len(posts)})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form':form})
        
    
