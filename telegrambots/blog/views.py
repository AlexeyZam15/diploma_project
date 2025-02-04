from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from . import models
from django.utils import lorem_ipsum

from . import forms


def get_context():
    categories = models.Category.objects.all()
    pop_articles = models.Article.get_published_posts().order_by('ar_views')[:5]
    return {
        'cats': categories,
        'pop_posts': pop_articles,
        'search_form': forms.SearchForm,
        'tags': models.Tag.objects.all(),
    }


def index(request):
    context = get_context()
    category_articles = [
        {'posts': models.Article.get_published_posts().filter(category=category).all(), 'cat': category}
        for category in context['cats']]
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
    form = forms.CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', post_id)
    context = get_context()
    context['title'] = post.title
    context['post'] = post
    context['form'] = form
    post.views += 1
    post.save()
    return render(request, 'blog/blog-detail.html', context)


def all_posts(request):
    context = get_context()
    search_query = request.GET.get('search', '')
    if search_query:
        context['title'] = f'Поиск по запросу: "{search_query}"'
        context['search_query'] = search_query
        context['posts'] = models.Article.get_published_posts().filter(Q(title__icontains=search_query) |
                                                                       Q(description__icontains=search_query) |
                                                                       Q(content__icontains=search_query))
    else:
        context['title'] = 'Все статьи'
        context['posts'] = models.Article.get_published_posts()
    context['search'] = search_query
    paginator = Paginator(context['posts'], 4)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['page'] = int(page_number)
    return render(request, 'blog/blog-list-01.html', context)


def show_category(request, category_title):
    context = get_context()
    category = get_object_or_404(models.Category, title=category_title)
    context['title'] = category.title
    posts = models.Article.get_published_posts().filter(category=category)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['page'] = int(page_number)
    context['text'] = category.description
    category.views += 1
    category.save()
    return render(request, 'blog/blog-list-01.html', context)


def show_tag(request, tag_slug):
    context = get_context()
    tag = get_object_or_404(models.Tag, slug=tag_slug)
    posts = models.Article.get_published_posts().filter(tags=tag)
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)
    context['title'] = tag.title
    context['page_obj'] = page_obj
    context['page'] = int(page_number)
    context['tag'] = tag
    context['text'] = tag.description
    tag.views += 1
    tag.save()
    return render(request, 'blog/category-01.html', context)


@login_required
def add_post(request):
    form = forms.ArticleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(author=request.user)
            return redirect('post', post.id)
    context = get_context()
    context['title'] = 'Добавить статью'
    context['form'] = form
    context['action'] = 'Создать'
    return render(request, 'blog/form_create.html', context)


@login_required
def change_post(request, post_id):
    post = get_object_or_404(models.Article, id=post_id)
    form = forms.ArticleForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post', post_id)
    context = get_context()
    context['title'] = 'Редактировать статью'
    context['form'] = form
    context['action'] = 'Сохранить'
    return render(request, 'blog/form_create.html', context)


def page_not_found(request, exception):
    return HttpResponseNotFound("Page not found")
