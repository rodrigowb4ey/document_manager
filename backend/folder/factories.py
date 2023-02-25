import factory
from faker import Faker

from utils.tools import get_random_user

fake = Faker('pt-br')


def fake_folder_name():
    random_word_list = fake.words(nb=2)
    random_word = ' '.join(random_word_list)

    return random_word


class FolderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'folder.Folder'

    name = factory.LazyFunction(fake_folder_name)
    owner = factory.LazyFunction(get_random_user)
