from django import template
from blogs.models import Post

register = template.Library()

@register.inclusion_tag('blogs/menu_foot.html')
def show_foot(menu_class='post-entry-sidebar'):
    posts = Post.objects.all().order_by('-id')[:3]
    return {'posts': posts, 'menu_class': menu_class}
