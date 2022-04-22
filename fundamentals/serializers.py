from rest_framework import serializers


class DerivateSerializer(serializers.Serializer):
    funct = serializers.CharField(max_length=255)


class IntegrateSerializer(serializers.Serializer):
    funct = serializers.CharField(max_length=255)
