from .serializers import HelloSerializer
from rest_framework import status, viewsets, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from static.Api import api


class HelloApiView(APIView):
    serializer = HelloSerializer
    code = 200

    def get(self, request):
        api = ['GET', 'POST', 'PATCH', 'DELETE']
        return Response({'code': self.code, 'message': self.message, 'data': api})

    def post(self, request):
        serial = self.serializer(data=request.data)

        if serial.is_valid():
            name = serial.validated_data.get('name')
            data = f'Hello {name}'
        else:
            self.code = status.HTTP_400_BAD_REQUEST
            data = serial.errors

        return api(self.code, data)

    def put(self, request, pk=None):
        data = "PUT"
        return api(self.code, data)

    def patch(self, request, pk=None):
        data = "PATCH"
        return api(self.code, data)

    def delete(self, request, pk=None):
        data = "DELETE"
        return api(self.code, data)


class HelloViewSet(viewsets.ViewSet):
    code = 200
    serializer_class = HelloSerializer

    def list(self, request):
        data = ['Hello', 'World']
        return api(self.code, data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            data = f'Hello {name}'
        else:
            self.code = status.HTTP_400_BAD_REQUEST
            data = serializer.errors

        return api(self.code, data)

    def retrieve(self, request, pk=None):
        data = "GET"
        return api(self.code, data)

    def update(self, request, pk=None):
        data = "PUT"
        return api(self.code, data)

    def partial_update(self, request, pk=None):
        data = "PATCH"
        return api(self.code, data)

    def destroy(self, request, pk=None):
        data = "DELETE"
        return api(self.code, data)
