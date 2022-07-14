from rest_framework import serializers
from document.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(required=False, view_name='user-detail', read_only=True)
    
    class Meta:
        model = Document
        fields = ['uuid', 'name', 'content', 'owner', 'created_at']
