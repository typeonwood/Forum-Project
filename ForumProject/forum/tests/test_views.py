from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Category, Thread, ThreadVotes
from .. import serializers
from rest_framework import status
from django.contrib.auth.models import User
import json

class TestCategoryViews(APITestCase):
    def setUp(self):
        self.payload = {'title': 'whales'}

    def test_list_viewer(self):
        response = self.client.get(reverse('categories-list'))
        category_list = Category.objects.all()
        serialized = serializers.CategoryViewerSerializer(category_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('categories-list'))
        category_list = Category.objects.all()
        serialized = serializers.CategoryAdminSerializer(category_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_unauth(self):
        response = self.client.post(
            reverse('categories-list'),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('categories-list'),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCategoryDetailView(APITestCase):
    def setUp(self):
        self.whales = Category.objects.create(title='whales')
        self.payload = {'title': 'dolphins'}

    def test_update_admin(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse('categories-detail', kwargs={'pk': self.whales.pk}),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_admin(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('categories-detail', kwargs={'pk': self.whales.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth(self):
        response = self.client.put(
            reverse('categories-detail', kwargs={'pk': self.whales.pk}),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestThreadListView(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='whales')

    def test_list_viewer(self):
        response = self.client.get(reverse('thread-list', kwargs={'category': self.category.pk}))
        thread_list = Thread.objects.filter(category=self.category.pk)
        serialized = serializers.ThreadViewerSerializer(thread_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('thread-list', kwargs={'category': self.category.pk}))
        thread_list = Thread.objects.filter(category=self.category.pk)
        serialized = serializers.ThreadAdminSerializer(thread_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_owner(self):
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('thread-list', kwargs={'category': self.category.pk}),
            data = json.dumps({'title': 'a thread', 'content': 'some slay content'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestThreadVotesViewSet(APITestCase):
    def setUp(self):
        self.origin = Thread.objects.create(
            title = 'a title',
            category = Category.objects.create(title='whales'),
            user = User.objects.create(username='test'),
            content = 'this is a post'
        )

    def test_list(self):
        self.user = User.objects.create_superuser(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('thread_votes-list', kwargs={'origin': self.origin.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('thread_votes-list', kwargs={'origin': self.origin.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauth_update(self):
        self.user = User.objects.create(username='testy', password='testy')
        vote = ThreadVotes.objects.create(thread=self.origin, user=self.user, upvote=True)
        response = self.client.patch(
            reverse('thread_votes-detail', kwargs={'origin': self.origin.pk, 'pk': vote.pk}),
            data = json.dumps({'upvote': False}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_update(self):
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        vote = ThreadVotes.objects.create(thread=self.origin, user=self.user, upvote=True)
        response = self.client.patch(
            reverse('thread_votes-detail', kwargs={'origin': self.origin.pk, 'pk': vote.pk}),
            data = json.dumps({'upvote': False}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_delete(self):
        user = User.objects.create(username='testy', password='testy')
        vote = ThreadVotes.objects.create(thread=self.origin, user=user, upvote=True)
        self.user = User.objects.create_superuser(username='testy1', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse('thread_votes-detail', kwargs={'origin': self.origin.pk, 'pk': vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_delete(self):
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        vote = ThreadVotes.objects.create(thread=self.origin, user=self.user, upvote=True)
        response = self.client.delete(
            reverse('thread_votes-detail', kwargs={'origin': self.origin.pk, 'pk': vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)