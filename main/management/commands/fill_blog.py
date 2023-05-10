from django.core.management import BaseCommand

from main.models import Article, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = Category.objects.create(title='Lorem Ipsum')

        articles = ['News one', 'New two', 'New three']
        for item in articles:
            Article.objects.create(
                title=item,
                body='Lorem ipsum',
                category=category
            )
