from django.core.management.base import BaseCommand
from document.factories import DocumentFactory


class Command(BaseCommand):
    help = "Populating fake database for development"

    def add_arguments(self, parser):
        parser.add_argument('num_of_instances', type=int, nargs='?', default=10)
    
    def handle(self, *args, **kwargs):
        num_of_instances = kwargs.get('num_of_instances', None)
        DocumentFactory.create_batch(num_of_instances)
        print(f"Populating fake database!")
