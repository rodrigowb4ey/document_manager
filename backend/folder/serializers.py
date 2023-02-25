from django.contrib.auth.models import User
from rest_framework import serializers

from folder.models import Folder


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(), view_name='user-detail'
    )

    class Meta:
        model = Folder
        fields = [
            'url',
            'uuid',
            'name',
            'owner',
            'created_at',
        ]
