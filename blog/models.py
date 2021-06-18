from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    likes = models.IntegerField(default=0)
    class Meta:
        ordering = ['-date', 'title']
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse("show_detail_post", args=[self.id])
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlikes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postlikes')
    

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date']
    def __str__(self) -> str:
        return f'{self.post.title} Comment'