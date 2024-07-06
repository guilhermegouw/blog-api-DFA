from rest_framework import serializers


class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
