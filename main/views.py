from django.shortcuts import render

from main.models import Article


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    context = {
        'object_list': Article.objects.all()[:3]
    }
    return render(request, 'main/index.html')


def blog(request):
    context = {
        'object_list': Article.objects.all()
    }
    return render(request, 'main/blog.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/contact.html')
