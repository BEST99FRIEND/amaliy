from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('comments/', views.CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('api/', include(router.urls)),
]
