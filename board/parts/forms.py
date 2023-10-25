
from django import forms
from .models import Ads


class AdsForm(forms.ModelForm):
    class Meta:
        image = forms.ImageField()
        model = Ads
        fields = [
            'title',
            'text',
            'author',
            'categories',
            'image',
        ]

        labels = {
            'author' : 'Автор',
            'categories' : 'Категория',
            'image' : 'Изображение',
            'title' : 'Заголовок',
            'text' : 'Содержание',
        }
