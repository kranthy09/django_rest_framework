from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostException,
                                InvalidCommentContent
                               )
from fb_post.utils import create_comment


class CreateCommentRequestclass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class CreateCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return CreateCommentRequestclass(**validated_data)

class CreateCommentResponseclass:
    def __init__(self, comment_id):
        self.comment_id = comment_id


class CreateCommentResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateCommentResponseclass(**validated_data)



@api_view(['POST'])
def get_create_comment_view(request, post_id):
    request_serializer = CreateCommentRequestSerializer(data = request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            comment_id = create_comment(
                            user_id=request_object.user_id,
                            post_id=post_id,
                            comment_content = request_object.content
                         )
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        except InvalidCommentContent:
            return Response(status=400)
        
        response_object = CreateCommentResponseclass(
                              comment_id=comment_id
                          )
        response_serializer = CreateCommentResponseSerializer(response_object)
        return Response(response_serializer.data, status=200)


"""
continue with @api_view(['POST'])
some error in views/__init__.py for get_create_comment_view
"""