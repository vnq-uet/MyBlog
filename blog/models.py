from django.db import models

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