from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidCommentException,
                                InvalidReplyContent
                               )
from fb_post.utils import reply_to_comment


class ReplytoCommentRequestclass:
    def __init__(self, user_id, content):
        self.user_id = user_id
        self.content = content


class ReplytoCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return ReplytoCommentRequestclass(**validated_data)


class ReplytoCommentResponseclass:
    def __init__(self, reply_id):
        self.reply_id = reply_id


class ReplytoCommentResponseSerializer(serializers.Serializer):
    reply_id = serializers.IntegerField()

    def create(self, validated_data):
        return ReplytoCommentResponseclass(**validated_data)


@api_view(['POST'])
def get_reply_to_comment_view(request, comment_id):
    request_serializer = ReplytoCommentRequestSerializer(data=request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            reply_id = reply_to_comment(
                user_id=request_object.user_id,
                comment_id = comment_id,
                reply_content = request_object.content
            )
        except InvalidUserException:
            return Response(status=404)
        except InvalidCommentException:
            return Response(status=404)
        except InvalidReplyContent:
            return Response(status=400)
        response_object = ReplytoCommentResponseclass(
                reply_id=reply_id
        )
        response_serializer = ReplytoCommentResponseSerializer(response_object)
        return Response(response_serializer.data, status=201)
