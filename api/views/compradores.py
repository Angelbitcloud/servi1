from cerberus import Validator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


from ..models.compradores import Compradores

class CompradoresApi(APIView):
    def post(self,request):
        validator=Validator({
            'nombre':{'required':True,'type':'string','empty':False},
            'apellido':{'required':True,'type':'string','empty':False},
            'direccion':{'required':True,'type':'string','empty':False},
            'ciudad':{'required':True,'type':'string','empty':False},
            'email':{'required':True,'type':'string','empty':False},
        })
        if not validator.validate(request.data):
            return Response({'data':validator.errors},status=status.HTTP_400_BAD_REQUEST)
        
        request.data['username']=request.data['email']
        request.data['password']="123456789"

        if Compradores.objects.filter(username=request.data['email']):
            return Response({'data':'usuario con email ya existente'},status=status.HTTP_409_CONFLICT)

        comprador=Compradores.objects.create(**request.data)
        return Response({'ID':comprador.pk},status=status.HTTP_201_CREATED)

    def get(self,request):
        compradores=Compradores.objects.filter(is_deleted=False).values('pk','nombre','apellido','ciudad','direccion','latitud','longitud')
        return Response(compradores,status=status.HTTP_200_OK)

#clase para manejor un solo registro
class SpecificCompradoresApi(APIView):
    def get(self,request,*args,**kwargs):
        comprador=Compradores.objects.filter(pk=kwargs['id'],is_deleted=False).values('pk','nombre','apellido','ciudad','direccion','latitud','longitud').first()
        return Response(comprador,status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        Compradores.objects.filter(pk=kwargs['id'],is_deleted=False).update(**{'is_deleted':True})
        return Response(status=status.HTTP_200_OK)
    
class GeoCodeCompradoresApi(APIView):
      def get(self,request):
        compradores=Compradores.objects.filter(is_deleted=False)
        for comprador in compradores:
            #aqui va la api
            pass 
        
        return Response(status=status.HTTP_200_OK)