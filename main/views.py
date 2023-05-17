from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from main.forms import CommentForm
from main.models import Article, Comment


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


class BlogDetail(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['form'] = CommentForm(initial={'article': self.kwargs.get('pk')})
        return context_data


class ContactView(TemplateView):
    template_name = 'main/contact.html'
    extra_context = {
        'title': 'Контакты'
    }

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        return super().get_context_data(**kwargs)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('main:article', args=[self.kwargs.get('pk')])
