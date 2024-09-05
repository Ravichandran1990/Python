from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Register
from .serializer import RegisterSerializer
from .authentication import JWTAuthentication
# from .models import Register

# Create your views here.
Register = get_user_model()
class RegisterView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer
    def post(self, request): 
        serializer =  RegisterSerializer(data = request.data)         
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            user = Register.objects.filter(email=email).first() 
            if user is None:
                serializer.save()
                print(request.data)
                # Generate the JWT token                 
                data = {'data': request.data}
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'message': "User Already Exist"})
        else:
            return Response({'Error': serializer._errors})
        
    def get(self, request):
        user = request
        serialized_user = RegisterSerializer(user).data
        return Response({'register': serialized_user })
    
class LoginView(APIView): 
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request): 
        #serializer =  RegisterSerializer(data = request.data)         
        email = request.data.get('email')
        if email:          
            user = Register.objects.filter(email=email).first() 
            if user is None:
                return Response({'message': "User not registered"})
            else:
                # Generate the JWT token
                request.data['name'] = user.name
                print(request.data)
                jwt_token = JWTAuthentication.create_jwt(request.data)
                data = {'token':jwt_token, 'data': request.data}
                return Response(data, status=status.HTTP_200_OK)       
        else:            
            return Response({'Error': "Email should be required"})
        

