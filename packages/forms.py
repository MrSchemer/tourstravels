from django import forms
from .models import booking

class Booking(forms.ModelForm):
    class Meta:
        model = booking
        fields = [
            'Firstname', 'middle_name', 'lastname', 'email', 
            'phone', 'address', 'pickup_location',
            'total_person', 'total_price', 'additional_prefrences', 'status'
        ]

