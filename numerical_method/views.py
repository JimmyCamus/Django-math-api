from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .bisection_method_package import bisection_method

class BisectionMethod(APIView):
    serializer_class = serializers.BisectionMethodSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        expression = serializer.validated_data.get('expression')
        min = serializer.validated_data.get('min')
        max = serializer.validated_data.get('max')
        epsilon = serializer.validated_data.get('epsilon')

        try:
            result = bisection_method(min, max, epsilon, expression)
            return Response({'result': result}, status= status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'There is not a solution'}, status= status.HTTP_200_OK)


