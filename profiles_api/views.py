from .serializers import HelloSerializer
from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    serializer = HelloSerializer
    code = 200
    message = "success"

    def get(self, request):
        api = ['GET', 'POST', 'PATCH', 'DELETE']
        return Response({'code': self.code, 'message': self.message, 'data': api})

    def post(self, request):
        serial = self.serializer(data=request.data)

        if serial.is_valid():
            name = serial.validated_data.get('name')
            data = f'Hello {name}'
        else:
            self.message = 'error'
            self.code = status.HTTP_400_BAD_REQUEST
            data = serial.errors

        return Response({'code': self.code, 'message': self.message, 'data': data})

    def put(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    code = 200
    message = "success"
    serializer_class = HelloSerializer

    def list(self, request):
        view = ['Hello', 'World']
        return Response({'code': self.code, 'message': self.message, 'data': view})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
        else:
            self.message = 'error'
            self.code = status.HTTP_400_BAD_REQUEST
            message = serializer.errors

        return Response({'code': self.code, 'message': self.message, 'data': message})

    def retrieve(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'GET'})

    def update(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'code': self.code, 'message': self.message, 'data': 'DELETE'})
