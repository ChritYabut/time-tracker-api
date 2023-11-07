"""
Serializers for TimeTask APIs
"""
from rest_framework import serializers

from core.models import TimeTask, Project
from project.serializers import ProjectSerializer

class TimeTaskSerializer(serializers.ModelSerializer):
    """ Serializer for timetasks. """
    total_hours = serializers.DecimalField(max_digits=5, decimal_places=2)
    project = ProjectSerializer()

    class Meta:
        model = TimeTask
        fields = ['id', 'project', 'hours', 'total_hours', 'task_description', 'date']
        read_only_fields = ['id', 'total_hours']

    def create(self, validated_data):
        """Create a timetask."""
        project_data = validated_data.pop('project')
        project_instance, created = Project.objects.get_or_create(**project_data)
        auth_user = self.context['request'].user

        timetask = TimeTask.objects.create(
            project=project_instance,
            **validated_data,
        )

        return timetask
