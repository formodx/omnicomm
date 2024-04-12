from rest_framework.routers import SimpleRouter

from .views import StatusViewSet
from .views import ReportViewSet


router = SimpleRouter()
router.register('status', StatusViewSet)
router.register('report', ReportViewSet)


urlpatterns = router.urls