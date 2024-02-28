from django import forms
from .models import Lead

class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields= ("firstname", "lastname", "company", "email", "phone", "comment", "priority", "status",)