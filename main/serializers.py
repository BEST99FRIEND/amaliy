from rest_framework import serializers

from .models import Author, Comment, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','full_name','email','bio')

class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),write_only=True)
    post_title = serializers.CharField(source='post.title',read_only=True)

    class Meta:
        model = Comment
        fields = ('id','post','post_title','name','text')

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(),write_only=True)
    author_name = serializers.CharField(source='author.full_name',read_only=True)

    class Meta:
        model = Post
        fields = ('id','title','content','author','author_name','views')

