from django import forms
from .models import Comment

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

    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Add a comment...'}), required=True)

    class Meta:
        model = Comment
        fields = ['body']
