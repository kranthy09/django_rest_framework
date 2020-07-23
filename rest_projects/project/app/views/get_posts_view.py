from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import serializers
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from app.models import Post

class PostsResponseclass:
    def __init__(self, post_id,posted_by,
                    content,posted_at
                ):
        self.post_id = post_id
        self.posted_by = posted_by
        self.content = content
        self.posted_at = posted_at


class PostsResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by = serializers.IntegerField()
    content = serializers.CharField(max_length=200)
    posted_at = serializers.DateTimeField()

    def create(self, validated_data):
        return PostsResponseclass(**validated_data)


@api_view(['GET'])
@authentication_classes([OAuth2Authentication])
def get_posts_view(request, user_id):
    
    posts = Post.objects.filter(
                posted_by=user_id
            )
    response_serializer = PostsResponseSerializer(posts, many=True)
    return Response(response_serializer.data, status=201)