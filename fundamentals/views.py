from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from sympy import diff, integrate, Symbol, parse_expr

from . import serializers

class Derivate(APIView):
    serializer_class = serializers.DerivateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status= status.HTTP_400_BAD_REQUEST
                )
        usr_funct = serializer.validated_data.get('funct')
        symbols = {'x': Symbol("x", real=True)}
        funct = parse_expr(usr_funct, symbols)

        derivated_function = diff(funct, symbols['x'])

        return Response({'derivate': str(derivated_function)})


class Integrate(APIView):
    serializer_class = serializers.IntegrateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status= status.HTTP_400_BAD_REQUEST
                )
        usr_funct = serializer.validated_data.get('funct')
        symbols = {'x': Symbol("x", real=True)}
        funct = parse_expr(usr_funct, symbols)

        integrated_function = integrate(funct, symbols['x'])

        return Response({'integrate': str(integrated_function)})
