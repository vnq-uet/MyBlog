from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

def show_list_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/list_post.html', {'posts':posts})

def show_detail_post(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    return render(request, 'posts/post_detail.html', {'post':post, 'form':form})