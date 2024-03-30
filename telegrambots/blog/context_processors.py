from .utils import menu, top_menu, user_top_menu


def get_blog_context(request):
    return {'menu': menu, 'top_menu': top_menu, 'user_top_menu': user_top_menu}
