from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from document.models import Document


class DocumentModelTestCase(TestCase):
    def setUp(self):
        self.test_user = User(
            username="testuser",
            email="user@test.com",
            is_superuser=True,
        )

        self.test_file = SimpleUploadedFile("test_file.pdf", b"test content")

        self.test_document = Document(
            name="Test Document",
            content=self.test_file,
            owner=self.test_user,
        )

    def test_valid_data_creates_document_instance(self):
        self.assertTrue(self.test_document)
        self.assertEqual(self.test_document.name, "Test Document")
        self.assertEqual(self.test_document.owner.username, "testuser")
        self.assertEqual(self.test_document.content, self.test_file)

    def test_document_repr_method(self):
        self.assertEqual(
            repr(self.test_document),
            (
                f"Document(name={self.test_document.name}, "
                f"owner={self.test_document.owner}, "
                f"content={self.test_document.content}, "
                f"created_at={self.test_document.created_at}, "
                f"uuid={self.test_document.uuid})"
            ),
        )

    def test_document_str_method(self):
        self.assertEqual(str(self.test_document), self.test_document.name)
