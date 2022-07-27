from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from blogs.models import Post, Comment, Category, CategoryByZone, Author, Tag


def home(request):
    # base
    posts = Post.objects.all()
    more_posts = Post.objects.all().order_by('?')[:3]
    post_slider = Post.objects.all().order_by('id')[:3]
    post_sidebar = Post.objects.all().order_by('-id')[:3]
    latest_posts = Post.objects.all().order_by('-id')[:3]
    zon_cats = CategoryByZone.objects.all()
    comments = Comment.objects.all()

    # pagination
    p = Paginator(posts, 4)
    page = request.GET.get('page')
    posts_ = p.get_page(page)

    context = {'more_posts': more_posts, 'post_slider': post_slider, 'post_sidebar': post_sidebar,
               'latest_posts': latest_posts, 'zon_cats': zon_cats, 'posts': posts_, 'p': p, 'comments': comments}
    return render(request, 'blogs/index.html', context)


def blog(request):
    # base
    posts = Post.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()

    # pagination
    p = Paginator(posts, 2)
    page = request.GET.get('page')
    posts_ = p.get_page(page)

    context = {'posts': posts_, 'p': p, 'category': category, 'tags': tags}
    return render(request, 'blogs/blog.html', context)


def blog_detail(request, slug):
    # base
    latest_posts = Post.objects.all().order_by('-id')[:3]
    related_posts = Post.objects.all().order_by('?')[:3]
    post = Post.objects.get(slug=slug)
    # main
    obj = Post.objects.get(slug=slug)
    obj.views += 1
    obj.save()
    # comment
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        Comment.objects.create(post=post, name=name, email=email, website=website, message=message)
        return redirect('blog-detail', slug)
    # commentcount = comments.count()
    # for comment in comments:
    #     comment.n = len(Post.objects.filter(comment=comment))

    return render(request, 'blogs/blog-single.html',
                  {'post': post, 'latest_posts': latest_posts, 'related_posts': related_posts, 'comments': comments})


def about(request):
    # base
    author = Author.objects.all()
    posts = Post.objects.all().order_by('-id')[:3]
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    return render(request, 'blogs/about.html', {'posts': posts_, 'p': p, 'author': author})


def get_category(request, id):
    # base
    category = Category.objects.get(pk=id)
    posts = Post.objects.filter(category=category)
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    context = {'category': category, 'posts': posts_, 'p': p}
    return render(request, 'blogs/category.html', context)


def category_zone(request, id):
    # base
    categorybyzone = CategoryByZone.objects.get(pk=id)
    posts = Post.objects.filter(categorybyzone=categorybyzone)
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)

    context = {'categorybyzone': categorybyzone, 'posts': posts_, 'p': p}
    return render(request, 'blogs/cat_zone.html', context)


def get_tag(request, id):
    # base
    tags = Tag.objects.all()
    tag = Tag.objects.get(pk=id)
    posts = Post.objects.filter(tag=tag)
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)

    return render(request, 'blogs/tag.html', {'tag': tag, 'posts': posts_, 'p': p, 'tags': tags})


def searched(request):
    q = request.GET.get('q')
    posts = Post.objects.filter(Q(title__icontains=q) |
                                Q(body__icontains=q) |
                                Q(category__title__icontains=q) |
                                Q(categorybyzone__title__icontains=q))
    context = {'posts': posts, 'q': q}
    return render(request, 'blogs/search.html', context)
