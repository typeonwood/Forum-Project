from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

router = SimpleRouter()
router.register(r'thread-votes', views.ThreadVotesViewSet, basename='thread_votes')
reply_router = routers.NestedSimpleRouter(router, r'thread-votes', lookup='thread')
reply_router.register(r'reply-votes', views.ReplyVotesViewSet, basename='reply_votes')

urlpatterns = [
    path('categories', views.CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='categories-detail'),
    path('categories/<int:category>/threads', views.ThreadListView.as_view(), name='thread-list'),
    path('categories/<int:category>/threads/<int:pk>', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('categories/<int:category>/threads/<int:thread>/replies', views.ReplyListView.as_view(), name='reply-list'),
    path('categories/<int:category>/threads/<int:thread>/replies/<int:pk>', views.ReplyDetailView.as_view(), name='reply-detail'),
    path('threads/<int:thread>/', include(router.urls)),
    path('replies/<int:reply>/', include(reply_router.urls)),
]