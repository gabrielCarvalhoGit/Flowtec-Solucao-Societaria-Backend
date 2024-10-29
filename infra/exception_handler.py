from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, NotFound, APIException

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, NotFound):
        return Response({'detail': str(exc.detail)}, status=status.HTTP_404_NOT_FOUND)

    if isinstance(exc, ValidationError):
        error_detail = str(exc.detail) if isinstance(exc.detail, dict) else str(exc.detail[0])
        return Response({'detail': error_detail}, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, APIException):
        return Response({'detail': str(exc)}, status=status.HTTP_400_BAD_REQUEST)

    return response