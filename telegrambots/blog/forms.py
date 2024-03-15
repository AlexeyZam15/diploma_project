from django import forms
from . import models


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'description', 'content', 'author', 'category', 'is_published', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-group'}),
            'image': forms.FileInput(attrs={'class': 'form-group'}),
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'content': 'Текст',
            'author': 'Автор',
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
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'author': 'Автор',
            'comment': 'Текст',
        }
