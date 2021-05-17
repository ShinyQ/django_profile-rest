from rest_framework import status
from rest_framework.response import Response


def api(code, data):
    message = "success"

    if code == 500 or code == 400:
        message = "error"
    elif code == 405:
        message = "method not allowed"

    return Response({'code': code, 'message': message, 'data': data})
