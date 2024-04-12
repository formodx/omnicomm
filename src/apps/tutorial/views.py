from rest_framework.viewsets import ModelViewSet

from .serializers import TutorialSerializer
from .models import Tutorial


class TutorialViewSet(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer