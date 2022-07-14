from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.TextField(max_length=80)
    content = models.FileField(upload_to="media/%Y/%m/%d")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'Document(name={self.name}, owner={self.owner}, created_at={self.created_at}, uuid={self.uuid})'

    def __str__(self):
        return f'{self.name}'
