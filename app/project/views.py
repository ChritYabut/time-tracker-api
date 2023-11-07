"""
Views for the project APIs.
"""
from rest_framework import viewsets

from core.models import Project
from project import serializers


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
