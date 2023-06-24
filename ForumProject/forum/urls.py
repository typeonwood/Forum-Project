from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'thread-votes', views.ThreadVotesViewSet, basename='thread_votes')
router.register(r'reply-votes', views.ReplyVotesViewSet, basename='reply_votes')

urlpatterns = [
    path('categories', views.CategoryListView.as_view(), name='categories-list'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='categories-detail'),
    path('categories/<int:category>/threads', views.ThreadListView.as_view(), name='thread-list'),
    path('categories/<int:category>/threads/<int:pk>', views.ThreadDetailView.as_view(), name='thread-detail'),
    path('categories/<int:category>/threads/<int:thread>/replies', views.ReplyListView.as_view(), name='reply-list'),
    path('categories/<int:category>/threads/<int:thread>/replies/<int:pk>', views.ReplyDetailView.as_view(), name='reply-detail'),
    path('id/<int:origin>/', include(router.urls)),
]