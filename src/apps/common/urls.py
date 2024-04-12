from rest_framework.routers import SimpleRouter

from .views import FileViewSet


router = SimpleRouter()
router.register('file', FileViewSet)


urlpatterns = router.urls