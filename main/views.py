from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from main.models import Article


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['object_list'] = Article.objects.all()[:3]
        return context_data


class BlogListView(ListView):
    model = Article
    extra_context = {
        'title': 'Главная страница'
    }


def blog_item(request, pk):
    context = {
        'object': Article.objects.get(pk=pk)
    }

    return render(request, 'main/blog_item.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have new message from {name}({email}): {message}')
    return render(request, 'main/contact.html')
