from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        return Response({'error': 'Something went wrong.'}, status=500)

    if isinstance(response.data, dict):
        if 'detail' in response.data:
            message = response.data['detail']
        else:
            pieces = []
            for field, value in response.data.items():
                if isinstance(value, list):
                    val = value[0] if value else 'invalid value'
                else:
                    val = value
                pieces.append(f'{field}: {val}')
            message = ' ; '.join(pieces)
        response.data = {'error': str(message)}
    else:
        response.data = {'error': str(response.data)}

    return response
