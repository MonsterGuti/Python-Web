from typing import override

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from books.models import Book, Tag


# class BookFormBasic(forms.Form):
#     title = forms.CharField(label='Title', max_length=100,
#                             widget=forms.TextInput(attrs={'placeholder': 'e.g Done'}))
#     price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2, min_value=0,
#                                widget=forms.NumberInput(attrs={'step': '2'}))
#     isbn = forms.CharField(label='ISBN', max_length=12, min_length=10)
#     genre = forms.ChoiceField(choices = Book.GenreChoices.choices,
#                               widget = forms.RadioSelect)
#     publishing_date = forms.DateField(initial=date.today,)
#     description = forms.CharField(label='Description',
#                                   widget=forms.Textarea)
#     image_url = forms.URLField(label='Image URL',)
#     publisher = forms.CharField(label='Publisher', max_length=100)

class BookFormBasic(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        exclude = ['slug']

        error_messages = {
            'title': {
                'max_length': 'The title is too long, no one is going to read that',
                'required': 'Hey you missed the title, no one is going to buy it',
            },
        },

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))

    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        if isbn.startswith('978'):
            raise ValidationError('ISBNs cannot start with 978')

    def clean(self):
        cleaned = super().clean()

        genre = cleaned.get('genre')
        pages = cleaned.get('pages')

        if genre == Book.GenreChoices.FICTION and pages < 10:
            raise ValidationError(f'Book genre is {genre} so pages must be at least 10')

    def save(self, commit=True):
        if self.publisher:
            self.publisher = self.publisher.capitalize()

        if commit:
            self.instance.save()

        return self.instance


class BookCreateForm(BookFormBasic):
    ...


class BookEditForm(BookFormBasic):
    ...


class BookDeleteForm(BookFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True


class BookSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search',
            'autofocus': 'true',
            'autocomplete': 'off',
        }),
        max_length=100,
    )
