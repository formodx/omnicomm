from rest_framework.viewsets import ModelViewSet

from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer