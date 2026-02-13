from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {
            'personal_photo': '',
            'name': '',
            'date_of_birth': '',
        }

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/YYYY'}),
            'name': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Name'}),
            'personal_photo': forms.URLInput(attrs={'type': 'url', 'placeholder': 'Photo'}),
        }

class PetDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True