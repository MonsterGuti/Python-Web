from datetime import date

from django import forms

from books.models import Book, Tag


# class BookFormBasic(forms.Form):
#     title = forms.CharField(label='Title', max_length=100,
#                             widget=forms.TextInput(attrs={'placeholder': 'e.g Done'}))
#     price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2, min_value=0,
#                                widget=forms.NumberInput(attrs={'step': '2'}))
#     isbn = forms.CharField(label='ISBN', max_length=12, min_length=10,)
#     genre = forms.ChoiceField(choices = Book.GenreChoices.choices,
#                               widget = forms.RadioSelect)
#     publishing_date = forms.DateField(initial=date.today,)
#     description = forms.CharField(label='Description',
#                                   widget=forms.Textarea,)
#     image_url = forms.URLField(label='Image URL',)
#     publisher = forms.CharField(label='Publisher', max_length=100,)

class BookFormBasic(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Book
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
