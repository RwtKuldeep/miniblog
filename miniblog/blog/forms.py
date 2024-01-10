from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Post


class User_RegistrationFom(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class User_Authentication(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        models = User


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    address = forms.TextInput()
    message = forms.Textarea()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', ]
