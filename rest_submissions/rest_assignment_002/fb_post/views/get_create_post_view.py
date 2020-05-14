from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostContent
                               )
from fb_post.utils.create_post import create_post


class CreatePostRequestclass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content

class CreatePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CreatePostRequestclass(**validated_data)

class CreatePostResponseclass:
    def __init__(self, post_id):
        self.post_id = post_id


class CreatePostResponseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreatePostResponseclass(**validated_data)


@api_view(['POST'])
def get_create_post_view(request):
    request_serializer = CreatePostRequestSerializer(data=request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            post_id = create_post(
                user_id=request_object.user_id,
                post_content=request_object.content
            )
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostContent:
            return Response(status=400)
        post_object = CreatePostResponseclass(
            post_id=post_id
        )
        response_serializer = CreatePostResponseSerializer(post_object)
        return Response(response_serializer.data, status=201)