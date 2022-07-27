from django.shortcuts import render, redirect
from contact.models import ContactUs
from blogs.models import Post
# Create your views here.
from contact.forms import ContactForm


def contact_us(request):
    # base
    latest_posts = Post.objects.all().order_by('-id')[:3]
    # contact
    # form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    context = {'latest_posts': latest_posts}
    return render(request, 'contact/contact.html', context)


# only simple way without form
# def contact_us(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         ContactUs.objects.create(name=name, phone=phone, email=email, message=message)
#         return redirect('contact_us')
#     return render(request, 'contact/contact.html')
