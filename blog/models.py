from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    class Meta:
        ordering = ['-date', 'title']
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date']
    def __str__(self) -> str:
        return f'{self.post.title} Comment'