from rest_framework import serializers


class Company(object):
    def __init__(self, name, registration_id):
        self.name = name                                # CHAR
        self.registration_id = registration_id          # UUID

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    registration_id = serializers.UUID()
