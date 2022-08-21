from django_filters import rest_framework as filters
from rest_framework import filters as restfilters
from rest_framework import viewsets

from document.models import Document
from document.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = (
        restfilters.SearchFilter,
        filters.DjangoFilterBackend,
    )
    filterset_fields = ["uuid", "name", "folder", "owner", "created_at"]
    search_fields = [
        "name",
    ]
