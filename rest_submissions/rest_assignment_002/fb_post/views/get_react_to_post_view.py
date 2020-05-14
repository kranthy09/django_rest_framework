from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidPostException,
                                InvalidReactionTypeException
                               )
from fb_post.utils import react_to_post
from fb_post.constants import ReactionChoice


class ReacttoPostRequestclass:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type


class ReacttoPostRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type\
        = serializers.ChoiceField(
            choices\
                =[reaction_type.value for reaction_type in ReactionChoice]
          )

    def create(self, validated_data):
        return ReacttoPostRequestclass(**validated_data)


@api_view(['POST'])
def get_react_to_post_view(request, post_id):
    request_serializer = ReacttoPostRequestSerializer(data=request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            react_to_post(
                user_id=request_object.user_id,
                post_id=post_id,
                reaction_type=request_object.reaction_type
            )
        except InvalidUserException:
            return Response(status=404)
        except InvalidPostException:
            return Response(status=404)
        except InvalidReactionTypeException:
            return Response(status=400)
        return Response(status=200)