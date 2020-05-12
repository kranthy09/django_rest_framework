from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (CreateSnippetResquest,
                          CreateSnippetResquestSerializers,
                          CreateSnippetResponseclass,
                          CreateSnippetResponseSerializer
                         )
from .models import Snippet


def create_snippet_in_db(title, code):

    return Snippet.objects.create(title=title, code=code)


@api_view(['POST'])
def create_snippet(request):

    serializer = CreateSnippetResquestSerializers(data=request.data)
    is_not_valid_data = not serializer.is_valid()
    if is_not_valid_data:
        Response(status=400)

    request_obj = serializer.save()
        
    response_obj = create_snippet_in_db(
        title = request_obj.title,
        code = request_obj.code
    )

    response_serializer = CreateSnippetResponseSerializer(response_obj)

    return Response(response_serializer.data)


@api_view(['GET'])
def get_list_of_snippets(request):

    Snippet.objects.bulk_create([
        Snippet(title="code_1", code="print(123"),
        Snippet(title="code_2", code="def add_two_numbers(a, b): return a+b")
    ])
    response_objects = Snippet.objects.all().order_by("-id")
    response_serializer = CreateSnippetResponseSerializer(response_objects, many=True)

    return Response(response_serializer.data)
