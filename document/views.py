from django_filters import rest_framework as filters
from rest_framework import filters as restfilters
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from document.models import Document
from document.serializers import DocumentSerializer
from utils.permissions import isOwner


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]
    filter_backends = (
        restfilters.SearchFilter,
        filters.DjangoFilterBackend,
    )
    filterset_fields = ["uuid", "name", "folder", "owner", "created_at"]
    search_fields = [
        "name",
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(owner=request.user)
        filtered_queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(filtered_queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)
