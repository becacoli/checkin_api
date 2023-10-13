from rest_framework import serializers
from .models import User, Classroom, Frequency, UserClassroom

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('__all__')
    
class ClassroomSerializer(serializers.ModelSerializer):
  class Meta:
    model = Classroom
    fields = ('__all__')
    
class FrequencySerializer(serializers.ModelSerializer):
  class Meta:
    model = Frequency
    fields = ('__all__')
    
class UserClassroomSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserClassroom
    fields = ('__all__')
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()