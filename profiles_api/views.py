from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):

    def get(self, request):
        api = ['GET', 'POST', 'PATCH', 'DELETE']
        return Response({'code': 200, 'message': 'success', 'data': api})
