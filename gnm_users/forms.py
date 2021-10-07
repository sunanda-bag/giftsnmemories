from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','email' ,'password1', 'password2')

class AppUserForm(forms.ModelForm):
    class Meta:
        model = GnmUser
        fields = ('address', 'mobile', 'city', 'pincode')

        widgets = {
            'mobile':forms.TextInput(attrs={'type':'tel',
                                            'pattern':'[0-9]{10}'}),
            'address':forms.TextInput(attrs={'class':'add-input'})
        }