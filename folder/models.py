from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models


class Folder(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.TextField(max_length=80)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __repr__(self):
        return (
            f"Folder(name={self.name}, "
            f"owner={self.owner}, "
            f"created_at={self.created_at}, "
            f"uuid={self.uuid})"
        )

    def __str__(self):
        return f"{self.name}"
