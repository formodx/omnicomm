from rest_framework.decorators import permission_classes, api_view
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class GetUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = None
    lookup_url_kwarg = None

    def get_object(self):
        # queryset = self.filter_queryset(self.get_queryset())

        # obj = get_object_or_404(queryset, {})

        # May raise a permission denied
        # self.check_object_permissions(self.request, obj)

        # return obj

        return self.request.user


@api_view(['POST'])
@permission_classes([])
def sign_in(request):
    # TODO: edit response
    email = request.data['email']
    password = request.data['password']

    user = User.objects.filter(email=email).first()

    if user is None:
        return Response(data='Email not found')

    if not user.check_password(raw_password=password):
        return Response(data='Password is not correct')

    token, created = Token.objects.get_or_create(user=user)

    return Response(data={'token': str(token)})


@api_view(['POST'])
def sign_out(request):
    # TODO: request.auth
    # TODO: edit response

    user = request.user

    token = Token.objects.filter(user=user)
    token.delete()

    return Response()


@api_view()
def get_users(request):
    # TODO: edit response

    data = []
    users = User.objects.all()

    for user in users:
        data.append({
            'email': user.email,
        })

    return Response(data=data)


@api_view()
def get_user_by_pk(request, pk):
    # TODO: edit response

    user = User.objects.filter(pk=pk).first()

    serializer = UserSerializer(instance=user)

    return Response(data=serializer.data)


@api_view(['POST'])
def change_password(request):
    # TODO: edit response
    old_password = request.data['old_password']
    new_password = request.data['new_password']
    confirmation_password = request.data['confirmation_password']

    user = request.user

    if not user.check_password(old_password):
        return Response(data='Old password is not correct')

    if new_password != confirmation_password:
        return Response(data='New password is not equal to confirmation password')

    user.set_password(new_password)
    user.save()

    return Response()