from django_filters import rest_framework as filters
from rest_framework import filters as restfilters
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from document.models import Document
from document.serializers import DocumentSerializer
from folder.models import Folder
from folder.serializers import FolderSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (
        restfilters.SearchFilter,
        filters.DjangoFilterBackend,
    )
    filterset_fields = ["uuid", "name", "owner", "created_at"]
    search_fields = [
        "name",
    ]

    @action(detail=True, serializer_class=DocumentSerializer)
    def documents(self, request, pk=None, *args, **kwargs):
        serializer_context = {"request": request}
        folder = self.get_object()
        documents_inside_folder = Document.objects.filter(folder=folder)
        documents_serialized = self.get_serializer(
            documents_inside_folder, many=True, context=serializer_context
        )

        return Response(documents_serialized.data)
