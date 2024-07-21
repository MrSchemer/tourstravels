from django import forms
from .models import ContactForm

class Contact(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']