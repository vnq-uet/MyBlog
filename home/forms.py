from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        pattern = re.compile(r'^\w+$')
        if len(pattern.findall(username)) == 0:
            raise forms.ValidationError('Tài khoản không hợp lệ!')
        return username

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password2 != password1:
                raise forms.ValidationError('Mật khẩu không hợp lệ!')
        return password2

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password1'])
        user.save()