from rest_framework.viewsets import ModelViewSet

from .serializers import StatusSerializer
from .serializers import ReportSerializer
from .models import Status
from .models import Report


class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)