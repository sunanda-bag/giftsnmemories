from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
from order.models import *


class CardMessageForm(forms.ModelForm):
    class Meta:
        model = CardMessage
        fields = ('recipient', 'sender', 'card_content_front', 'card_content_back')

        widgets = {
            'recipient':forms.TextInput(attrs={'class':'recipient',}),
            'sender':forms.TextInput(attrs={'class':'sender'})
        }