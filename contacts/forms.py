from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    hobbies = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Separate hobbies with commas'}))

    class Meta:
        model = Contact
        fields = ['name', 'address', 'phone', 'email', 'hobbies']
