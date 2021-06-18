from django.shortcuts import render
from .models import Post, Like
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

def show_list_post(request):
    posts = Post.objects.all()
    return render(request, 'posts/list_post.html', {'posts':posts})

def show_detail_post(request, pk):
    liked = False
    if request.user.is_authenticated:
        user = request.user
        post = Post.objects.get(id=pk)
        if Like.objects.filter(user=user, post=post).exists():
            liked = True
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    return render(request, 'posts/post_detail.html', {'post': post, 'form': form, 'liked': liked})

@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    current_likes = post.likes
    if Like.objects.filter(user=user, post=post).exists():
        Like.objects.filter(user=user, post=post).delete()
        current_likes -= 1
    else:
        Like.objects.create(user=user, post=post)
        current_likes += 1
    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('show_detail_post', args=[post_id]))
        