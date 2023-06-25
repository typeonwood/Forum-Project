from rest_framework.test import APITestCase
from ..models import Category, Thread, Reply, ThreadVotes, ReplyVotes
from django.contrib.auth.models import User

class TestCategoryModel(APITestCase):
    def test_create(self):
        new_category = Category.objects.create(title='whales')
        category = Category.objects.get(pk=new_category.pk)
        self.assertEqual(new_category, category)


class TestThreadModel(APITestCase):
    def test_create(self):
        new_thread = Thread.objects.create(
            title = 'a title',
            category = Category.objects.create(title='whales'),
            user = User.objects.create(username='test'),
            content = 'this is a post'
        )
        thread = Thread.objects.get(pk=new_thread.pk)
        self.assertEqual(new_thread, thread)

class TestReplyModel(APITestCase):
    def test_create(self):
        new_reply = Reply.objects.create(
            thread = Thread.objects.create(
                title = 'a title',
                category = Category.objects.create(title='whales'),
                user = User.objects.create(username='test'),
                content = 'this is a post'
            ),
            user = User.objects.get(username='test'),
            content = 'this is some content'
        )
        reply = Reply.objects.get(pk=new_reply.pk)
        self.assertEqual(new_reply, reply)

class TestThreadVotesModel(APITestCase):
    def test_create(self):
        new_vote = ThreadVotes.objects.create(
            user = User.objects.create(username='test'),
            thread = Thread.objects.create(
                title = 'a title',
                category = Category.objects.create(title='whales'),
                user = User.objects.get(username='test'),
                content = 'this is a post'
            ),
            upvote = True
        )
        vote = ThreadVotes.objects.get(pk=new_vote.pk)
        self.assertEqual(new_vote, vote)

class TestReplyVotesModel(APITestCase):
    def test_create(self):
        new_vote = ReplyVotes.objects.create(
            user = User.objects.create(username='test'),
            reply = Reply.objects.create(
                thread = Thread.objects.create(
                    title = 'a title',
                    category = Category.objects.create(title='whales'),
                    user = User.objects.get(username='test'),
                    content = 'this is a post'
                ),
                user = User.objects.get(username='test'),
                content = 'this is some content'
            ),
            upvote = True
        )
        vote = ReplyVotes.objects.get(pk=new_vote.pk)
        self.assertEqual(new_vote, vote)
