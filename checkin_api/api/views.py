from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import User, Classroom, UserClassroom, Frequency
from .serializers import UserSerializer, ClassroomSerializer, FrequencySerializer, UserClassroomSerializer, LoginSerializer
# Create your views here.
class UserList(generics.ListCreateAPIView):
  serializer_class = UserSerializer  
  queryset  = User.objects.all()
  
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = UserSerializer
  queryset  = User.objects.all()
  lookup_field = 'id'

class ClassroomList(generics.ListCreateAPIView):
  serializer_class = ClassroomSerializer  
  queryset  = Classroom.objects.all()
  
class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ClassroomSerializer
  queryset  = Classroom.objects.all()
  lookup_field = 'id'
  
class FrequencyList(generics.ListCreateAPIView):
  serializer_class = FrequencySerializer  
  queryset  = Frequency.objects.all()
  
class FrequencyDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FrequencySerializer
  queryset  = Frequency.objects.all()
  lookup_field = 'id'
  
class UserClassroomList(generics.ListCreateAPIView):
  serializer_class = UserClassroomSerializer
  queryset  = UserClassroom.objects.all()
  
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(email=email, password=password)
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data)
            except User.DoesNotExist:
                return Response({"error": "Credenciais inválidas."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)