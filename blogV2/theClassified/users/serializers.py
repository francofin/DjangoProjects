from rest_framework import serializers
from .models import CustomUser, UserProfile



class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()
    user_security_identifier = serializers.CharField(max_length=500,read_only=True)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password', 'password2', 'user_security_identifier')

        extra_kwargs = {
            'first_name': {'required':True, 'allow_blank':False },
            'last_name': {'required':True, 'allow_blank':False },
            'email': {'required':True, 'allow_blank':False },
            'password': {'required':True, 'allow_blank':False, 'min_length':8 },
            'password2': {'required':True, 'allow_blank':False, 'min_length':8 },
        }

class UserProfileSerializer(serializers.ModelSerializer):
    resume = serializers.CharField(source='userprofile.resume')
    profile_picture = serializers.CharField(source='userprofile.profile_picture')
    user = serializers.StringRelatedField()
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_security_identifier = serializers.CharField(max_length=500,read_only=True)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'role', 'user_security_identifier')