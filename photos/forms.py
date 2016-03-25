from django import forms

from .models import Photo

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'content', )