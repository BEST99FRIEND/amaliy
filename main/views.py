from rest_framework import filters, generics, viewsets
from .models import Author, Comment, Post
from .permissions import IsAdminForCreateDelete
from .serializers import (
    AuthorSerializer,
    CommentSerializer,
    PostDetailSerializer,
    PostSerializer,
)


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.select_related('post').all()
    serializer_class = CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('comments').all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminForCreateDelete,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'content', 'author__full_name')
    ordering_fields = ('views', 'created_at')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer
