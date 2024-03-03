from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from blog import models

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
]

top_menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'},
]


def get_context():
    return {
        'menu': menu,
        'posts': models.Article.objects.all(),
        'cats': models.Category.objects.all(),
        'top_menu': top_menu,
    }


def index(request):
    context = get_context()
    context['title'] = 'Главная страница'
    return render(request, 'blog/index.html', context)


def about(request):
    context = get_context()
    context['title'] = 'О сайте'
    return render(request, 'blog/about.html', context)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def add_page(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def register(request):
    return HttpResponse('Регистрация')


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
