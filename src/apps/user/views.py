from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from .serializers import SignInSerializer
from .serializers import SignOutSerializer
from .serializers import ChangePasswordSerializer


class GetUpdateAPIView(GenericAPIView):
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.get_serializer(instance=request.user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        serializer = self.get_serializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SignInAPIView(GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response(data={'token': str(token)}, status=status.HTTP_200_OK)


class SignOutAPIView(GenericAPIView):
    serializer_class = SignOutSerializer

    def post(self, request):
        token = request.auth

        Token.objects.get(key=token).delete()

        return Response(data=None, status=status.HTTP_200_OK)


class ChangePasswordAPIView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        if not user.check_password(serializer.validated_data['old_password']):
            return Response(data=None, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response(data=None, status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_in(request):
    pass


@api_view(['POST'])
def sign_out(request):
    pass


@api_view()
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(data=serializer.data)


@api_view()
def get_user_by_pk(request, pk):
    try:
        user = User.objects.get(id=pk)
    except:
        return Response(data=None)

    serializer = UserSerializer(instance=user)

    return Response(data=serializer.data)