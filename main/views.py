from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView

from main.forms import CommentForm, ArticleForm
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


class BlogCreateView(UserPassesTestMixin, CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('main:blog')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.author = self.request.user
            self.object.save()

        return super().form_valid(form)


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm

    def test_func(self):
        return self.request.user.is_staff and self.get_object().author == self.request.user


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
