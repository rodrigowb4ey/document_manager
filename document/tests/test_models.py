from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from document.models import Document


class DocumentModelTestCase(TestCase):
    def setUp(self):
        self.test_user = User(
            username="testuser",
            email="user@test.com",
            is_superuser=True,
        )

        self.test_file = SimpleUploadedFile(
            "test_file.pdf",
            b"test content"
        )

    def test_valid_data_creates_document_instance(self):
        """Test that checks if a Document instance is created when valid data is given."""
        test_document = Document(
            name="Test Document",
            content=self.test_file,
            owner=self.test_user,
        )
        self.assertTrue(test_document)
        self.assertEqual(test_document.name, "Test Document")
        self.assertEqual(test_document.owner.username, "testuser")
        self.assertEqual(test_document.content, self.test_file)
