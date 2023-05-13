from rest_framework import serializers
from .models import Access_level, Vehicle, Tyre, Fault, Service_schedule, Maintenance_type,Work_order,Maintenance_record,CustomUser


#Creating general Serializers
class Access_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_level
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = '__all__'

class FaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fault
        fields = '__all__'

class Service_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_schedule
        fields = '__all__'

class Maintenance_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_type
        fields = '__all__'

class Work_orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work_order
        fields = '__all__'

class Maintenance_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_record
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  


#Creating Authentication Serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


#Sign-up serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'PhoneNo')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        PhoneNo = attrs.get('PhoneNo', '')

        if not username.isalnum():
            raise serializers.ValidationError(self.default_error_messages)
        return attrs
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    

#Login serializer
class LoginSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = CustomUser.objects.get(username=obj['username'])
        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'tokens')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = auth.authenticate(username=username, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')
        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }


#Logout serializer
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')