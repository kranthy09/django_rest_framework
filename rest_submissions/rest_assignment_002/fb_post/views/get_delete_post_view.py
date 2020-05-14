from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostException,
                                UserCannotDeletePostException
                               )
from fb_post.utils import delete_post


class DeletePostRequestclass:
    def __init__(self, user_id):
        self.user_id = user_id


class DeletePostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeletePostRequestclass(**validated_data)

@api_view(['POST'])
def get_delete_post_view(request, post_id):
    request_serializer = DeletePostRequestSerializer(data=request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            delete_post(
                user_id=request_object.user_id,
                post_id=post_id
            )
        except InvalidPostException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        except UserCannotDeletePostException:
            return Response(status=403)
        return Response(status=200)