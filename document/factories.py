import random
import factory
from faker import Faker
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile


fake = Faker('pt-br')


def fake_document_name():
    random_word_list = fake.words(nb=4)
    random_word = "_".join(random_word_list)
    fake_name = f"{random_word}.pdf"

    return fake_name


def get_random_user():
    return random.choice(User.objects.all())


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "document.Document"

    name = factory.LazyFunction(fake_document_name)
    content = factory.LazyAttribute(
        lambda _: ContentFile(
            factory.django.FileField()._make_data(
                {"width": 800, "height": 600}
            ), fake_document_name()
        ),
    )
    owner = factory.LazyFunction(get_random_user)
