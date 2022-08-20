from rest_framework import viewsets

from folder.models import Folder
from folder.serializers import FolderSerializer


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
