from django import forms
from flats_app.models import Flat


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        exclude = ("owner", )
