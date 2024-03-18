from django.conf import settings
from django.conf.urls.static import static
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
                  path("posts/<int:post_id>/", views.show_post, name='post'),
                  path("posts/create/", views.add_post, name='add_post'),
                  path("posts/<int:post_id>/update/", views.change_post, name='change_post'),
                  path("posts/tag/<slug:tag>/", views.show_tag, name='tag_posts'),
                  path("posts/categories/<slug:category>/", views.show_category, name='category'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
