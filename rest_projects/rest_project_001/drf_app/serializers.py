# serializers.py

from rest_framework import serializers
from .views import Comment


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=200)

    def validate_title(self, value):
        
        is_post_not_about_django = 'django' not in value.lower()
        if is_post_not_about_django:

            raise serializers.ValidationError('Blog post is not about Django')

        return value
