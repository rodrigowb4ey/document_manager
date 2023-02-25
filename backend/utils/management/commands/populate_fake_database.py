from django.core.management.base import BaseCommand

from document.factories import DocumentFactory
from folder.factories import FolderFactory


class Command(BaseCommand):
    help = 'Populating fake database for development'

    def add_arguments(self, parser):
        parser.add_argument(
            '--folders', type=int, help='Indicate number of folders'
        )

        parser.add_argument(
            '--documents', type=int, help='Indicate number of documents'
        )

    def handle(self, *args, **kwargs):
        if kwargs['folders'] and kwargs['documents']:
            num_of_folders = kwargs['folders']
            num_of_documents = kwargs['documents']
            FolderFactory.create_batch(num_of_folders)
            DocumentFactory.create_batch(num_of_documents)
        else:
            FolderFactory.create_batch(5)
            DocumentFactory.create_batch(25)

        print('Populating fake database!')
