from rest_framework.serializers import ModelSerializer, SerializerMethodField, UniqueTogetherValidator, IntegerField
from .models import Category, Thread, Reply, ThreadVotes, ReplyVotes
from django.contrib.auth.models import User

class CategoryViewerSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class CategoryAdminSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class ReplyViewerSerializer(ModelSerializer):
    upvotes = SerializerMethodField()
    class Meta:
        model = Reply
        fields = ['user', 'date_time_added', 'upvotes', 'content']
    def get_upvotes(self, obj):
        if ReplyVotes.objects.filter(reply=obj.id).exists():    
            upvotes = ReplyVotes.objects.filter(reply=obj.id, upvote=True).count()
            downvotes = ReplyVotes.objects.filter(reply=obj.id, upvote=False).count()
            total = upvotes - downvotes
            return total
        else:
            return 0

class ReplyOwnerSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ['content']

class ReplyAdminSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ThreadListSerializer(ModelSerializer):
    upvotes = SerializerMethodField()
    class Meta:
        model = Thread
        fields = ['title', 'category', 'user', 'date_time_added', 'upvotes', 'locked']
    def get_upvotes(self, obj):
        if ThreadVotes.objects.filter(thread=obj.id).exists():    
            upvotes = ThreadVotes.objects.filter(thread=obj.id, upvote=True).count()
            downvotes = ThreadVotes.objects.filter(thread=obj.id, upvote=False).count()
            total = upvotes - downvotes
            return total
        else:
            return 0

class ThreadViewerSerializer(ThreadListSerializer):
    replies = SerializerMethodField()
    class Meta(ThreadListSerializer.Meta):
        fields = ['title', 'category', 'user', 'date_time_added', 'upvotes', 'locked', 'content', 'replies']
    def get_replies(self, obj):
        if Reply.objects.filter(thread=obj.id).exists():
            queryset = Reply.objects.filter(thread=obj.id).order_by('date_time_added')
            serialized = ReplyViewerSerializer(queryset, many=True)
            return serialized.data
        else:
            return ''

class ThreadOwnerSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = ['title', 'content']

class ThreadAdminListSerializer(ThreadListSerializer):
    replies = SerializerMethodField()
    class Meta(ThreadListSerializer.Meta):
        fields = '__all__'
    def get_replies(self, obj):
        if Reply.objects.filter(thread=obj.id).exists():
            return Reply.objects.filter(thread=obj.id).count()
        else: return 'No replies'


class ThreadAdminSerializer(ModelSerializer):
    replies = SerializerMethodField()
    class Meta(ThreadViewerSerializer.Meta):
        model = Thread
        fields = ['id', 'title', 'category', 'user', 'date_time_added', 'locked', 'content', 'media_link', 'replies']
    def get_replies(self, obj):
        if Reply.objects.filter(thread=obj.id).exists():
            queryset = Reply.objects.filter(thread=obj.id)
            serialized = ReplyAdminSerializer(queryset, many=True)
            return serialized.data
        else:
            return ''
        
class ThreadVotesSerializer(ModelSerializer):
    class Meta:
        model = ThreadVotes
        fields = ['upvote', 'thread', 'user']
        

class ThreadVotesUpdateSerializer(ModelSerializer):
    class Meta:
        model = ThreadVotes
        fields = ['upvote']

class ThreadVotesAdminSerializer(ModelSerializer):
    class Meta:
        model = ThreadVotes
        fields = '__all__'

class ReplyVotesSerializer(ModelSerializer):
    class Meta:
        model = ReplyVotes
        fields = ['upvote', 'reply', 'user']

class ReplyVotesUpdateSerializer(ModelSerializer):
    class Meta:
        model = ReplyVotes
        fields = ['upvote']


class ReplyVotesAdminSerializer(ModelSerializer):
    class Meta:
        model = ReplyVotes
        fields = '__all__'


