from django import template
from blogs.models import Category, Post

register = template.Library()

@register.inclusion_tag('blogs/menu_cat.html')
def show_menu(menu_class='dropdown-menu'):
    post = Post.objects.all()
    categories = Category.objects.all()
    category = Category.objects.filter(post=post)
    return {'categories': categories, 'menu_class': menu_class, 'category': category}
