"""
URL mapping for the timetask app.
"""
from django.urls import(
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from timetask import views


router = DefaultRouter()
router.register('timetask', views.TimeTaskViewSet)

app_name = 'timetask'

urlpatterns = [
    path('', include(router.urls)),
]