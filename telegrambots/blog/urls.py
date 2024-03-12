from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index, name='home'),
    path("contact/", views.contact, name='contact'),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path("about/", views.about, name='about'),
    path("posts/", views.all_posts, name='posts'),
    path("posts/<int:post_id>", views.show_post, name='post'),
    path("posts/", views.add_post, name='add_post'),
    path("categories/<int:category_id>", views.show_category, name='category'),
]
