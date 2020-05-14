from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fb_post.exceptions import InvalidPostException
from fb_post.utils import get_post

class UserReponseclass:
    def __init__(self, name, user_id, profile_pic):
        self.name = name
        self.user_id = user_id
        self.profile_pic = profile_pic


class UserResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    user_id = serializers.IntegerField()
    profile_pic = serializers.URLField()

    def create(self, validated_data):
        return UserReponseclass(**validated_data)


class ReactionsResponseclass:
    def __init__(self, count, type):
        self.count = count
        self.type = type


class ReactionsResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    type = serializers.ListField()

    def create(self, validated_data):
        return ReactionsResponseclass(**validated_data)


class RepliesResponseclass:
    def __init__(self, comment_id, commenter, commented_at,
                 comment_content, reactions
                ):
        self.comment_id = comment_id
        self.commenter = commenter
        self.commented_at = commented_at
        self.comment_content = comment_content
        self.reactions = reactions


class RepliesResponseSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserResponseSerializer()
    commented_at = serializers.DateTimeField()
    comment_content = serializers.CharField()
    reactions = ReactionsResponseSerializer()


class CommentsResponseclass(RepliesResponseclass):
    def __init__(self, comment_id, commenter, commented_at,
                 comment_content,reactions,
                 replies_count, replies
                ):
        super().__init__(comment_id, commenter, commented_at,
                         comment_content, reactions
                        )
        self.replies_count = replies_count
        self.replies = replies


class CommentsResponseSerializer(RepliesResponseSerializer):
    replies_count = serializers.IntegerField()
    replies = RepliesResponseSerializer(many=True)

    def create(self, validated_data):
        return CommentsResponseclass(**validated_data)

class PostRepsonseclass:
    def __init__(self, post_id, posted_by, posted_at,
                 reactions, comments
                ):
        self.post_id = post_id
        self.posted_by = posted_by
        self.posted_at = posted_at
        self.reactions = reactions
        self.comments = comments

class PostRepsonseSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    posted_by = UserResponseSerializer()
    posted_at = serializers.DateTimeField()
    reactions = ReactionsResponseSerializer()
    comments = CommentsResponseSerializer(many=True)

    def create(self, **validated_data):
        return PostResponseclass(**validated_data)


@api_view(['GET'])
def get_post_view(request, post_id):
    try:
        data = get_post(post_id)
    except InvalidPostException:
        return Response(status=404)
    response_object = PostRepsonseclass(
        post_id = data['post_id'],
        posted_by = data['posted_by'],
        posted_at = data['posted_at'],
        reactions = data['reactions'],
        comments = data['comments']
    )
    response_serializer = PostRepsonseSerializer(response_object)
    return Response(response_serializer.data, status=200)
 