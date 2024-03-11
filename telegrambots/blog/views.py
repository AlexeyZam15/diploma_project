from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from blog import models
from django.utils import lorem_ipsum

menu = [
    {'title': 'Главная', 'url_name': 'home'},
    {'title': 'Статьи', 'url_name': 'posts'},
]

top_menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Регистрация', 'url_name': 'register'},
    {'title': 'Войти', 'url_name': 'login'},
]


def get_context():
    categories = models.Category.objects.all()
    pop_articles = models.Article.get_published_posts().order_by('-views')[:5]
    return {
        'menu': menu,
        'cats': categories,
        'top_menu': top_menu,
        'pop_posts': pop_articles
    }


def index(request):
    context = get_context()
    category_articles = {category.title: models.Article.get_published_posts().filter(category=category).all()[:4] for category in
                         context['cats']}
    context['c_posts'] = category_articles
    context['title'] = 'Главная'
    return render(request, 'blog/index.html', context)


def about(request):
    context = get_context()
    context['title'] = 'О сайте'
    context['content'] = lorem_ipsum.words(200)
    return render(request, 'blog/about.html', context)


def contact(request):
    context = get_context()
    context['title'] = 'Обратная связь'
    return render(request, 'blog/contact.html', context)


def login(request):
    context = get_context()
    context['title'] = 'Вход'
    return render(request, 'blog/login.html', context)


def register(request):
    context = get_context()
    context['title'] = 'Регистрация'
    return render(request, 'blog/register.html', context)


def show_post(request, post_id):
    post = get_object_or_404(models.Article, id=post_id)
    context = get_context()
    context['title'] = post.title
    context['post'] = post
    return render(request, 'blog/blog-detail.html', context)


def all_posts(request):
    context = get_context()
    context['title'] = 'Все статьи'
    context['posts'] = models.Article.get_published_posts()
    return render(request, 'blog/blog-list-01.html', context)


def add_post(request):
    context = get_context()
    context['title'] = 'Добавить статью'
    return render(request, 'blog/add_post.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
