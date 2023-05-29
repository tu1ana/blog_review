from django.conf import settings

from main.models import Article
from django.core.cache import cache


def get_cached_top_articles():
    key = 'top_articles'
    queryset = Article.objects.all()[:3]
    if settings.LOW_CACHED:
        top_articles = cache.get(key)
        if top_articles is None:
            top_articles = queryset
            cache.set(key, top_articles)
        return top_articles
    return queryset
