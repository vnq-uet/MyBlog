from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.author = kwargs.pop('author', None)
    #     self.post = kwargs.pop('post', None)
    #     super().__init__(*args, **kwargs)

    # def save(self):
    #     comment = super().save(commit=False)
    #     comment.author = self.author
    #     comment.post = self.post
    #     comment.save()

    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add a comment...', 'class': 'form-control'}), required=True)

    class Meta:
        model = Comment
        fields = ['body']

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100, required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    image = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'description', 'image']
