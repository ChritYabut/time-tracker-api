"""
Serializers for project APIs
"""
from rest_framework import serializers
from core.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']
        read_only_fields = ['id']
