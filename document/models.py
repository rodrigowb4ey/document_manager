from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models

from folder.models import Folder


class Document(models.Model):
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.TextField(max_length=80)
    content = models.FileField(upload_to="%Y/%m/%d")
    folder = models.ForeignKey(
        Folder, on_delete=models.CASCADE, blank=True, null=True
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __repr__(self):
        return (
            f"Document(name={self.name}, "
            f"owner={self.owner}, "
            f"content={self.content}, "
            f"folder={self.folder}, "
            f"created_at={self.created_at}, "
            f"uuid={self.uuid})"
        )

    def __str__(self):
        return f"{self.name}"
