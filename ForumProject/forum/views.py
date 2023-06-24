from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Category, Thread, Reply, ThreadVotes, ReplyVotes
from .serializers import CategoryViewerSerializer, CategoryAdminSerializer, ReplyViewerSerializer, ReplyOwnerSerializer, ReplyAdminSerializer, ThreadViewerSerializer, ThreadOwnerSerializer, ThreadAdminSerializer, ThreadVotesSerializer, ReplyVotesSerializer, ThreadVotesAdminSerializer, ReplyVotesAdminSerializer
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
        return super(CategoryListView, self).get_permissions()

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
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(ThreadListView, self).get_permissions()

    def list(self, request, category=None):
        if self.request.user.is_superuser:
            queryset = Thread.objects.filter(category=Category.objects.get(pk=category))
            serialized = ThreadAdminSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        else:
            queryset = Thread.objects.filter(category=Category.objects.get(pk=category))
            serialized = ThreadViewerSerializer(queryset, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)
        
    def create(self, request, category=None):
        if self.request.user.is_superuser:
            queryset = self.request.POST
            serialized = ThreadAdminSerializer(queryset)
            if serialized.is_valid():
                serialized.save(user=self.request.user, category=Category.objects.get(pk=category))
                return Response('Your post has been submitted', status=status.HTTP_201_CREATED)
            else:
                return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = self.request.POST
            serialized = ThreadOwnerSerializer(data=queryset)
            if serialized.is_valid():
                serialized.save(user=self.request.user, category=Category.objects.get(pk=category))
                return Response('Your post has been submitted', status=status.HTTP_201_CREATED)
            else:
                return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
            

class ThreadDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Thread.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super(ThreadDetailView, self).get_permissions()
    
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
    def get_permissions(self):
        if self.request.method == 'POST':
            pass
        else:
            self.permission_classes = [IsAdminUser]

    def create(self, request, thread=None):
        queryset = self.request.POST
        serialized = ReplyOwnerSerializer(data=queryset)
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
        return super(ThreadDetailView, self).get_permissions()
    

class ThreadVotesViewSet(ModelViewSet):
    queryset = ThreadVotes.objects.all()
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
        else:
            return ThreadVotesSerializer
        
    def create(self, request, origin, category):
        queryset = self.request.POST.copy()
        queryset['thread'] = origin
        queryset['user'] = self.request.user.id
        serialized = ThreadVotesSerializer(data=queryset)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, origin, category):
        queryset = self.request.body.copy()
        queryset['thread'] = origin
        queryset['user'] = self.request.user.id
        serialized = ThreadVotesSerializer(data=queryset)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        

class ReplyVotesViewSet(ModelViewSet):
    queryset = ReplyVotes.objects.all()
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAdminUser]
        elif self.request.method =='POST':
            self.permission_classes = [IsAuthenticated]
        elif self.request.method == 'PUT' or 'PATCH':
            self.permission_classes = [OwnerPermission]
        else:
            self.permission_classes = [IsAdminUser | OwnerPermission]
        return super(ReplyVotesViewSet, self).get_permissions()
    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ReplyVotesAdminSerializer
        else:
            return ReplyVotesSerializer
        
    def create(self, request, origin, category):
        queryset = self.request.POST.copy()
        queryset['reply'] = origin
        queryset['user'] = self.request.user.id
        serialized = ReplyVotesSerializer(data=queryset)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, origin, category):
        queryset = self.request.body.copy()
        queryset['reply'] = origin
        queryset['user'] = self.request.user.id
        serialized = ReplyVotesSerializer(data=queryset)
        if serialized.is_valid():
            serialized.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response('Invalid data...', status=status.HTTP_400_BAD_REQUEST)

