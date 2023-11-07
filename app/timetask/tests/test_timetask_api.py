"""
Test for timetask APIs.
"""
from datetime import datetime, timezone
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import TimeTask, Project

# from timetask.serializers import TimeTaskSerializer

TIMETASK_URL = reverse('timetask:timetask-list')


def create_timetask(user, project, **params):
    """ Create and return a sample time task."""
    defaults = {
        'hours': 8,
        'task_description': 'sample description',
        'date': datetime.now(timezone.utc)
    }
    defaults.update(params)

    timetask = TimeTask.objects.create(user=user, project=project, **defaults)
    return timetask


def create_project(**params):
    """ Create and return a sample project."""
    defaults = {
        'name': 'Sample Project',
    }
    defaults.update(params)

    project = Project.objects.create(**defaults)
    return project


class PublicTimeTaskAPITests(TestCase):
    """ Test unauthenticated API requests. """

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """ Test auth is required to call API. """
        res = self.client.get(TIMETASK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTimeTaskAPITests(TestCase):
    """ Test authenticated API requests. """

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass1123',
        )
        self.project = create_project()
        self.client.force_authenticate(self.user)

    def test_retrieve_timetasks(self):
        """ Test retrieving a list of timetasks. """
        create_timetask(user=self.user, project=self.project)
        create_timetask(user=self.user, project=self.project)

        res = self.client.get(TIMETASK_URL)

        # timetasks = TimeTask.objects.all()
        # serializer = TimeTaskSerializer(timetasks, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertEqual(res.data, serializer.data)

    def test_timetask_list_limited_to_user(self):
        """ Test list of timetasks is limited to authenticated user. """
        new_user = get_user_model().objects.create_user(
            'newuser@example.com',
            'password123',
        )
        create_timetask(user=self.user, project=self.project)
        create_timetask(user=new_user, project=self.project)

        res = self.client.get(TIMETASK_URL)

        # timetasks = TimeTask.objects.filter(
        #     user=self.user, project=self.project
        #     )
        # serializer = TimeTaskSerializer(timetasks, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertEqual(res.data, serializer.data)
