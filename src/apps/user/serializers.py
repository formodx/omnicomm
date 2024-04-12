from django.contrib.auth import authenticate

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'middle_name', 'last_name',
            'email', 'password',
            'gender', 'avatar'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Unable to log in with provided credentials')

        attrs['user'] = user

        return attrs


class SignOutSerializer(serializers.Serializer):
    pass


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirmation_password = serializers.CharField()

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        confirmation_password = attrs.get('confirmation_password')

        if new_password != confirmation_password:
            raise serializers.ValidationError('Passwords must be same')

        return attrs