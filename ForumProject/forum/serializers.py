from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.validators import UniqueValidator
from .models import Category, Thread, Reply

class CategoryViewerSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
        validators = [UniqueValidator(queryset=Category.objects.filter(fieldname='title'))]

class CategoryAdminSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        validators = [UniqueValidator(queryset=Category.objects.filter(fieldname='title'))]  

class ReplyViewerSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ['thread', 'user', 'date_time_added', 'content']

class ReplyOwnerSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ['thread', 'user', 'content']

class ReplyAdminSerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ThreadViewerSerializer(ModelSerializer):
    reply = SerializerMethodField()
    class Meta:
        model = Thread
        fields = ['title', 'category', 'user', 'date_time_added', 'locked', 'content']
    def get_reply(self, obj):
        queryset = Reply.objects.filter(thread=obj.id)
        serialized = ReplyViewerSerializer(queryset)
        return serialized.data

class ThreadOwnerSerializer(ModelSerializer):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'user', 'content',]

class ThreadAdminSerializer(ThreadViewerSerializer):
    class Meta(ThreadViewerSerializer.Meta):
        model = Thread
        fields = '__all__'

