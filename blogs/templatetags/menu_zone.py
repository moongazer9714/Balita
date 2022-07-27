from django import template
from blogs.models import CategoryByZone, Post

register = template.Library()

@register.inclusion_tag('blogs/menu_zone.html')
def show_zone(menu_class='dropdown-menu'):
    post = Post.objects.all()
    cat_zones = CategoryByZone.objects.all()
    cat_zone = CategoryByZone.objects.filter(post=post)
    return {'cat_zones': cat_zones, 'menu_class': menu_class, 'cat_zone': cat_zone}
