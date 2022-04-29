from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .bisection_method_package import bisection_method
from .newton_raphson_package import newton_rapson_method
from .fixed_point_method_package import fixed_method


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
            return Response({'result': result}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': 'There is not a solution'}, status=status.HTTP_200_OK)


class NewtonRaphsonMethod(APIView):
    serializer_class = serializers.NewtonRaphsonSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        funct = serializer.validated_data.get('funct')
        derivate = serializer.validated_data.get('derivate')
        initial_point = serializer.validated_data.get('initial_point')
        epsilon = serializer.validated_data.get('epsilon')

        try:
            result = newton_rapson_method(
                initial_point, funct, derivate, epsilon)
            return Response({'result': result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'There is not a solution'}, status=status.HTTP_200_OK)


class FixedPointMethod(APIView):
    serializer_class = serializers.FidexPointSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        expression = serializer.validated_data.get('expression')
        initial_point = serializer.validated_data.get('initial_point')
        epsilon = serializer.validated_data.get('epsilon')

        try:
            result = fixed_method(initial_point, epsilon, expression)
            return Response({'result': result}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'There is not a solution'}, status=status.HTTP_200_OK)
