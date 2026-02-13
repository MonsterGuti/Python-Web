from django import forms

from reviews.models import Review


class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewCreateForm(ReviewFormBasic):
    ...


class ReviewEditForm(ReviewFormBasic):
    ...


class ReviewDeleteForm(ReviewFormBasic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True
