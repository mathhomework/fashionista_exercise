from django import forms
from faq.models import Fashionista


class FashionistaForm(forms.ModelForm):
    class Meta:
        model = Fashionista
        # fields = ['name', 'email', 'phone_number', 'fb', 'twitter', 'blog', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'fb': forms.TextInput(attrs={'placeholder': 'facebook'}),
            'twitter': forms.TextInput(attrs={'placeholder': 'Twitter'}),
            'blog': forms.TextInput(attrs={'placeholder': 'Blog'}),
            'desc': forms.Textarea(
                attrs={'placeholder': 'Tell us about your style.'}),
        }