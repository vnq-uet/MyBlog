from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
        user.save()