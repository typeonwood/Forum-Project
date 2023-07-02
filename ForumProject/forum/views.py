from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Category, Thread, Reply, ThreadVotes, ReplyVotes
from .serializers import CategoryViewerSerializer, CategoryAdminSerializer, ReplyViewerSerializer, ReplyOwnerSerializer, ReplyAdminSerializer, ThreadViewerSerializer, ThreadOwnerSerializer, ThreadAdminSerializer, ThreadVotesSerializer, ReplyVotesSerializer, ThreadVotesAdminSerializer, ReplyVotesAdminSerializer, ThreadVotesUpdateSerializer, ReplyVotesUpdateSerializer, ThreadListSerializer, ThreadAdminListSerializer
from rest_framework import status
from .permissions import OwnerPermission

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer  
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def list(self, request):
        if self.request.user.is_superuser:
            queryset = Category.objects.all()
            serialized = CategoryAdminSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            queryset = Category.objects.all()
            serialized = CategoryViewerSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK) 


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAdminSerializer 
    permission_classes = [IsAdminUser]


class ThreadListView(ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadAdminSerializer
    ordering_fields = ['date_time_added', 'threadvotes', 'replies']
    search_fields = ['title', 'user', 'content']
    filterset_fields = {'date_time_added': ['gte', 'lte'], 'user': ['exact'], 'locked': ['exact']}
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def list(self, request, category=None):
        if self.request.user.is_superuser:
            queryset = self.filter_queryset(self.get_queryset()).filter(category=Category.objects.get(pk=category))
            serialized = ThreadAdminListSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            queryset = self.filter_queryset(self.get_queryset()).filter(category=Category.objects.get(pk=category))
            serialized = ThreadListSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        
    def create(self, request, category=None):
        if self.request.user.is_superuser:
            serialized = ThreadAdminSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save(user=self.request.user, category=Category.objects.get(pk=category))
                return Response('Your post has been submitted', status=status.HTTP_201_CREATED)
            else:
                return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        else:
            serialized = ThreadOwnerSerializer(data=request.data)
            if serialized.is_valid(raise_exception=True):
                serialized.save(user=self.request.user, category=Category.objects.get(pk=category))
                return Response('Your post has been submitted', status=status.HTTP_201_CREATED)
            else:
                return Response(self.request.POST, status=status.HTTP_400_BAD_REQUEST)
            

class ThreadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super().get_permissions()
    
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ThreadAdminSerializer
        elif self.request.method == 'GET':
            return ThreadViewerSerializer
        else:
            return ThreadOwnerSerializer
        

class ReplyListView(ListCreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplyAdminSerializer
    ordering_fields = ['date_time_added', 'replyvotes', 'replies']
    search_fields = ['user', 'thread', 'content']
    filterset_fields = {'date_time_added': ['gte', 'lte'], 'user': ['exact'], 'thread': ['exact']}
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def create(self, request, category, thread=None):
        serialized = ReplyOwnerSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save(user=self.request.user, thread=Thread.objects.get(pk=thread))
            return Response('Your reply has been submitted', status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        

class ReplyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reply.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ReplyAdminSerializer
        elif self.request.method == 'GET':
            return ReplyViewerSerializer
        else:
            return ReplyOwnerSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super().get_permissions()
    

class ThreadVotesViewSet(ModelViewSet):
    queryset = ThreadVotes.objects.all()
    search_fields = ['user', 'thread']
    filterset_fields = ['upvote', 'user', 'thread']
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser]
        elif self.request.method =='POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == 'PUT' or 'PATCH':
            self.permission_classes = [OwnerPermission]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super(ThreadVotesViewSet, self).get_permissions()
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ThreadVotesAdminSerializer
        elif self.request.method == 'PUT' or 'PATCH':
            return ThreadVotesUpdateSerializer
        else:
            return ThreadVotesSerializer
        
    def create(self, request, thread=None):
        queryset = self.request.POST.copy()
        queryset['thread'] = thread
        queryset['user'] = self.request.user.id
        serialized = ThreadVotesSerializer(data=queryset)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        

class ReplyVotesViewSet(ModelViewSet):
    queryset = ReplyVotes.objects.all()
    search_fields = ['user', 'reply']
    filterset_fields = ['upvote', 'user', 'reply']
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser]
        elif self.request.method =='POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == 'PUT' or 'PATCH':
            self.permission_classes = [OwnerPermission]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super(ModelViewSet, self).get_permissions()
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ReplyVotesAdminSerializer
        elif self.request.method == 'PUT' or 'PATCH':
            return ReplyVotesUpdateSerializer
        else:
            return ReplyVotesSerializer
        
    def create(self, request, thread_pk=None, reply=None):
        queryset = self.request.POST.copy()
        queryset['reply'] = reply
        queryset['user'] = self.request.user.id
        serialized = ReplyVotesSerializer(data=queryset)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Oops...couldn't vote", status=status.HTTP_400_BAD_REQUEST)