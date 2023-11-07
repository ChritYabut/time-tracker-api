"""
Views for the timetask APIs.
"""
from django_filters import rest_framework as filters
from django.db.models import Sum, DecimalField, Value
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import TimeTask
from timetask import serializers


class TimeTaskFilter(filters.FilterSet):
    date = filters.DateFilter(lookup_expr="gte")
    class Meta:
        model = TimeTask
        fields = ['project__name', 'date']


class TimeTaskViewSet(viewsets.ModelViewSet):
    """View for manage timetask APIs."""
    serializer_class = serializers.TimeTaskSerializer
    queryset = TimeTask.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TimeTaskFilter

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        """Retrieve time tasks for authenticated user."""
        queryset = self.filter_queryset(self.queryset.filter(user=self.request.user))
        total_hours = queryset.aggregate(total_hours=Sum('hours'))
        # Annotate the queryset with total_hours using aggregation function
        queryset = queryset.annotate(total_hours=Value(total_hours.get('total_hours'), output_field=DecimalField()))

        return queryset.order_by('id')

    def perform_create(self, serializer):
        """Create a new time task."""
        serializer.save(user=self.request.user)
