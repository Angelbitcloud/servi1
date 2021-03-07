from cerberus import Validator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models.compradores import Compradores

class CompradoresApi(APIView):
    validator=Validator({
        'nombre':{'required':True,'type':'string','empty':False},
        'apellido':{'required':True,'type':'string','empty':False},
        'direccion':{'required':True,'type':'string','empty':False},
        'ciudad':{'required':True,'type':'string','empty':False},
    })
    if not validator.validate(request.data):
        return Response({'data':validator.errors},status=status.HTTP_400_BAD_REQUEST)