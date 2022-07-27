from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog-detail'),

    path('category/<int:id>/', views.get_category, name='get-category'),
    path('categoryzone/<int:id>/', views.category_zone, name='category-zone'),
    path('tag/<int:id>/', views.get_tag, name='get-tag'),
    path('search/', views.searched, name='search'),
]