from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Category, Thread, ThreadVotes, Reply, ReplyVotes
from .. import serializers
from rest_framework import status
from django.contrib.auth.models import User
import json

class TestCategoryViews(APITestCase):
    def setUp(self):
        self.payload = {'title': 'whales'}
        self.admin = User.objects.create_superuser(username='testy', password='testy')
        self.category_list = Category.objects.all()

    def test_list_viewer(self):
        response = self.client.get(reverse('categories-list'))
        serialized = serializers.CategoryViewerSerializer(self.category_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.user = self.admin
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('categories-list'))
        serialized = serializers.CategoryAdminSerializer(self.category_list, many=True)
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
        self.user = self.admin
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
        self.admin = User.objects.create_superuser(username='testy', password='testy')
        self.kwargs = {'pk': self.whales.pk}

    def test_update_admin(self):
        self.user = self.admin
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            reverse('categories-detail', kwargs=self.kwargs),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_admin(self):
        self.user = self.admin
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('categories-detail', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth(self):
        response = self.client.put(
            reverse('categories-detail', kwargs=self.kwargs),
            data = json.dumps(self.payload),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestThreadListView(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='whales')
        self.thread_list = Thread.objects.filter(category=self.category.pk)
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        self.kwargs = {'category': self.category.pk}

    def test_list_viewer(self):
        response = self.client.get(reverse('thread-list', kwargs=self.kwargs))
        serialized = serializers.ThreadListSerializer(self.thread_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_admin(self):
        self.user.is_superuser
        response = self.client.get(reverse('thread-list', kwargs=self.kwargs))
        serialized = serializers.ThreadAdminListSerializer(self.thread_list, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_owner(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('thread-list', kwargs=self.kwargs),
            data = json.dumps({'title': 'a thread', 'content': 'some slay content'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestThreadDetailView(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='whales')
        self.user = User.objects.create(username='test')
        self.client.force_authenticate(user=self.user)
        self.thread = Thread.objects.create(
            title = 'a title',
            category = self.category,
            user = self.user,
            content = 'this is a post'
        )
        self.reply1 = Reply.objects.create(thread=self.thread, user=self.user, content='some content')
        self.reply2 = self.reply1
        self.kwargs = {'category': self.category.pk, 'pk': self.thread.pk}
        
    def test_retrieve(self):
        response = self.client.get(reverse('thread-detail', kwargs=self.kwargs))
        serialized = serializers.ThreadViewerSerializer(self.thread)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_retrieve(self):
        self.user.is_superuser
        response = self.client.get(reverse('thread-detail', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_update(self):
        self.client.logout()
        response = self.client.put(
            reverse('thread-detail', kwargs=self.kwargs),
            data = json.dumps({'title': 'nothing', 'content': 'less than nothing'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_update(self):
        response = self.client.put(
            reverse('thread-detail', kwargs=self.kwargs),
            data = json.dumps({'title': 'nothing', 'content': 'also nothing'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete(reverse('thread-detail', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestReplyListView(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='whales')
        self.user = User.objects.create(username='test')
        self.client.force_authenticate(user=self.user)
        self.thread = Thread.objects.create(
            title = 'a title',
            category = self.category,
            user = self.user,
            content = 'this is a post'
        )
        self.reply1 = Reply.objects.create(thread=self.thread, user=self.user, content='some content')
        self.reply2 = self.reply1
        self.kwargs = {'category': self.category.pk, 'thread': self.thread.pk}

    def test_admin_get(self):
        self.user = User.objects.create_superuser(username='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('reply-list', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_get(self):
        self.client.logout()
        response = self.client.get(reverse('reply-list', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create(self):
        response = self.client.post(
            reverse('reply-list', kwargs=self.kwargs),
            data = json.dumps({'content': 'some content'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestReplyDetailView(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(title='whales')
        self.user = User.objects.create(username='test')
        self.client.force_authenticate(user=self.user)
        self.thread = Thread.objects.create(
            title = 'a title',
            category = self.category,
            user = self.user,
            content = 'this is a post'
        )
        self.reply1 = Reply.objects.create(thread=self.thread, user=self.user, content='some content')
        self.kwargs = {'category': self.category.pk, 'thread': self.thread.pk, 'pk': self.reply1.pk}

    def test_retrieve(self):
        response = self.client.get(reverse('reply-detail', kwargs=self.kwargs))
        serialized = serializers.ReplyViewerSerializer(self.reply1)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauth_update(self):
        self.client.logout()
        response = self.client.put(
            reverse('reply-detail', kwargs=self.kwargs),
            data = json.dumps({'content': 'some dumb content'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_update(self):
        response = self.client.put(
            reverse('reply-detail', kwargs=self.kwargs),
            data = json.dumps({'content': 'some dumb content'}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.user.is_superuser = True
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('reply-detail', kwargs=self.kwargs))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestThreadVotesViewSet(APITestCase):
    def setUp(self):
        self.thread = Thread.objects.create(
            title = 'a title',
            category = Category.objects.create(title='whales'),
            user = User.objects.create(username='test', password='test'),
            content = 'this is a post'
        )
        self.user = User.objects.get(username='test')
        self.client.force_authenticate(user=self.user)
        self.vote = ThreadVotes.objects.create(upvote=True, user=self.user, thread=self.thread)

    def test_list(self):
        self.user = User.objects.create_superuser(username='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('thread_votes-list', kwargs={'thread': self.thread.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.vote.delete()
        self.user.is_superuser = True
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            reverse('thread_votes-list', kwargs={'thread': self.thread.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_create(self):
        response = self.client.post(
            reverse('thread_votes-list', kwargs={'thread': self.thread.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_update(self):
        self.client.logout()
        response = self.client.patch(
            reverse('thread_votes-detail', kwargs={'thread': self.thread.pk, 'pk': self.vote.pk}),
            data = json.dumps({'upvote': False}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_update(self):
        response = self.client.put(
            reverse('thread_votes-detail', kwargs={'thread': self.thread.pk, 'pk': self.vote.pk}),
            data = json.dumps({'upvote': False}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_delete(self):
        self.user = User.objects.create_superuser(username='testy1', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse('thread_votes-detail', kwargs={'thread': self.thread.pk, 'pk': self.vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_delete(self):
        response = self.client.delete(
            reverse('thread_votes-detail', kwargs={'thread': self.thread.pk, 'pk': self.vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestReplyVotesViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testy', password='testy')
        self.client.force_authenticate(user=self.user)
        self.thread = Thread.objects.create(
            title = 'a title',
            category = Category.objects.create(title='whales'),
            user = self.user,
            content = 'this is a post'
        )
        self.reply = Reply.objects.create(
            thread = self.thread,
            user = self.user,
            content = 'this is a post'
        )
        self.vote = ReplyVotes.objects.create(upvote=False, user=self.user, reply=self.reply)

    def test_list(self):
        self.user = User.objects.create_superuser(username='testy1', password='testy')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('reply_votes-list', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        self.vote.delete()
        response = self.client.post(
            reverse('reply_votes-list', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bad_create(self):
        response = self.client.post(
            reverse('reply_votes-list', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauth_update(self):
        self.client.logout()
        response = self.client.patch(
            reverse('reply_votes-detail', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk, 'pk': self.vote.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_auth_update(self):
        response = self.client.put(
            reverse('reply_votes-detail', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk, 'pk': self.vote.pk}),
            data = json.dumps({'upvote': True}),
            content_type = 'application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_delete(self):
        self.user.is_superuser = True
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            reverse('reply_votes-detail', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk, 'pk': self.vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_delete(self):
        response = self.client.delete(
            reverse('reply_votes-detail', kwargs={'reply': self.reply.pk, 'thread_pk': self.thread.pk, 'pk': self.vote.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

