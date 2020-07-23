from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response


@api_view(["GET"])
@authentication_classes([OAuth2Authentication])
@protected_resource(['superuser'])
def dummy_view(request):
    print("Call to dummy_view")
    return Response()