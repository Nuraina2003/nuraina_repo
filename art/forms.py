from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class RegisterUserForm(UserCreationForm):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=255)
    mather_name = models.CharField(max_length=15)
    father_name = models.CharField(max_length=15)
    email = models.EmailField(blank=True, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=10)

    class Meta:
        model = User
        fields = ('__all__')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


class AddPostForm(forms.ModelForm):
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['category'].empty_label = "Таңдаңыз"

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = '__all__'
