from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import (InvalidUserException,
                                InvalidCommentException,
                                InvalidReactionTypeException
                               )
from fb_post.utils import react_to_comment
from fb_post.constants import ReactionChoice


class ReacttoCommentRequestclass:
    def __init__(self, user_id, reaction_type):
        self.user_id = user_id
        self.reaction_type = reaction_type


class ReacttoCommentRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    reaction_type\
        = serializers.ChoiceField(
            choices=[reaction.value for reaction in ReactionChoice]
          )

    def create(self, validated_data):
        return ReacttoCommentRequestclass(**validated_data)


@api_view(['POST'])
def get_react_to_comment_view(request, comment_id):
    request_serializer = ReacttoCommentRequestSerializer(data=request.data)
    is_valid_data = request_serializer.is_valid()
    if is_valid_data:
        request_object = request_serializer.save()
        try:
            react_to_comment(
                user_id=request_object.user_id,
                comment_id=comment_id,
                reaction_type=request_object.reaction_type
            )
        except InvalidUserException:
            return Response(status=404)
        except InvalidCommentException:
            return Response(status=404)
        except InvalidReactionTypeException:
            return Response(status=400)
        return Response(status=200)