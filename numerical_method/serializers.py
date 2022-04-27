from rest_framework import serializers
from sympy import Max

class BisectionMethodSerializer(serializers.Serializer):
    min = serializers.FloatField()
    max = serializers.FloatField()
    epsilon = serializers.FloatField()
    expression = serializers.CharField()
