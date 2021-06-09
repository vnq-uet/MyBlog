from django.shortcuts import render
from .models import Post
# Create your views here.

def show_list_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/list_post.html', {'posts':posts})

def show_detail_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post':post})