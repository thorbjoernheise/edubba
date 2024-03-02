from django import forms
from .models import Client

class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields= ("firstname", "lastname", "company", "email", "phone", "comment",)