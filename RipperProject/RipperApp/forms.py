from django import forms
from .models import Song


class RawSongForm(forms.Form):
    artist = forms.CharField(max_length=100,
                             widget=forms.TextInput()
                             )
    title = forms.CharField(max_length=100,
                            widget=forms.TextInput()
                            )
    genre = forms.ChoiceField(choices=Song.genreList)


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'audio/mpeg'}),
        label='Select a file',
        help_text='max. 42 megabytes'
    )