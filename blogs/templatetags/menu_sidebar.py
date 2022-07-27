from django import  template
from blogs.models import Author, Post, Tag, Category

register = template.Library()

@register.inclusion_tag('blogs/about_tpl.html')
def get_author(menu_class='sidebar-box'):
    author = Author.objects.all()
    return {'author': author, 'menu_class': menu_class}


@register.inclusion_tag('blogs/menu_popular.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blogs/menu_category.html')
def get_category():
    categories = Category.objects.all()
    for category in categories:
        category.n = len(Post.objects.filter(category=category))
    return {'categories': categories}

@register.inclusion_tag('blogs/menu_tag.html')
def get_tag():
    tags = Tag.objects.all()
    return {'tags': tags}
