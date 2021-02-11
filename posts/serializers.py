from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username',)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(source='author.username',)

    class Meta:
        fields = '__all__'
        model = Comment
