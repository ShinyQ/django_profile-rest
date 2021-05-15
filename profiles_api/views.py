from .serializers import HelloSerializer
from rest_framework import status
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

    def put(self, request):
        return Response({'code': self.code, 'message': self.message, 'data': 'PUT'})

    def patch(self, request):
        return Response({'code': self.code, 'message': self.message, 'data': 'PATCH'})

    def delete(self, request):
        return Response({'code': self.code, 'message': self.message, 'data': 'DELETE'})
