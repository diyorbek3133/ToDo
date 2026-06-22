from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from user.serializer import UserRegisterSerializer,LoginUserSerializer
from user.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
class LoginUser(APIView):
    serializer_class = LoginUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            refresh = RefreshToken.for_user(user)
            return Response({
                "user": user.username,
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)