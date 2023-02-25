import random

import factory
from django.core.files.base import ContentFile
from faker import Faker

from folder.factories import FolderFactory
from folder.models import Folder
from utils.tools import get_random_user

fake = Faker('pt-br')


def fake_document_name():
    random_word_list = fake.words(nb=4)
    random_word = '_'.join(random_word_list)
    fake_name = f'{random_word}.pdf'

    return fake_name


def get_random_folder():
    try:
        random_folder = random.choice(Folder.objects.all())
    except IndexError:
        random_folder = FolderFactory()

    return random_folder


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'document.Document'

    name = factory.LazyFunction(fake_document_name)
    folder = factory.LazyFunction(get_random_folder)
    content = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.FileField()._make_data(
                {'width': 800, 'height': 600}
            ),
            fake_document_name(),
        ),
    )
    owner = factory.LazyFunction(get_random_user)
