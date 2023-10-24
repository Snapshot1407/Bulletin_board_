from django.forms import ModelForm, CharField

from .models import Ads


class AdsForm(ModelForm):
    class Meta:
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