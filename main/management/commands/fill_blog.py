from django.core.management import BaseCommand

from main.models import Article


class Command(BaseCommand):

    def handle(self, *args, **options):
        articles = ['News one', 'New two', 'New three']
        for item in articles:
            Article.objects.create(
                title=item,
                body='Lorem ipsum'
            )
