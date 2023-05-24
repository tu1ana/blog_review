from django.conf import settings
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Article(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='статья')
    comment = models.TextField(verbose_name='комментарий')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} - {self.article}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('-created_at',)
