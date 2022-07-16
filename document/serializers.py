from django.contrib.auth.models import User
from rest_framework import serializers

from document.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name="user-detail"
    )

    class Meta:
        model = Document
        fields = ["url", "uuid", "name", "content", "owner", "created_at"]
