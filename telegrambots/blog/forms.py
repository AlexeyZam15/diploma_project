from django import forms
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'description', 'content', 'category', 'is_published', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-group'}),
            'image': forms.FileInput(attrs={'class': 'form-group'}),
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'content': 'Текст',
            'category': 'Категория',
            'is_published': 'Опубликовано',
            'image': 'Превью',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['author', 'comment']
        widgets = {
            'author': forms.Select(attrs={'class': 'form-group'}),
        }
        labels = {
            'author': 'Автор',
            'comment': 'Текст',
        }


class SearchForm(forms.Form):
    search_str = forms.CharField(max_length=100, required=False,
                                 widget=forms.TextInput(attrs={'class': 'f1-s-1 cl6 plh9 s-full p-l-25 p-r-45'}), label="")
    search_str.widget.attrs.update({'placeholder': 'Поиск'})
    search_str.widget.attrs.update({'type': 'text'})
    search_str.widget.attrs.update({'name': 'search'})
