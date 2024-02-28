from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Обучение', 'content': 'Контент Обучение', 'is_published': True, },
    {'id': 2, 'title': 'Работа', 'content': 'Контент Работа', 'is_published': False, },
    {'id': 3, 'title': 'Домашка', 'content': 'Контент Домашка', 'is_published': True, },
]

cats = ['Обучение', 'Работа', 'Домашка']


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cats': cats
    }
    return render(request, 'blog/index.html', context)


def about(request):
    context = {
        'title': 'О сайте',
        'menu': menu
    }
    return render(request, 'blog/about.html', context)


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def add_page(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
