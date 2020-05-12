from rest_framework import serializers


class CreateSnippetResquest:

    def __init__(self, code, title=''):
        self.title = title
        self.code = code


class CreateSnippetResquestSerializers(serializers.Serializer):

    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        
        return CreateSnippetResquest(**validated_data)


class CreateSnippetResponseclass:

    def __init__(self, id, code, title):
        self.id = id
        self.code = code
        self.title = title


class CreateSnippetResponseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(required=False, allow_blank=True,
                                  max_length=100
                                 )
    code = serializers.CharField(max_length=200)

    def create(self, validated_data):

        return CreateSnippetResponseclass(**validated_data)