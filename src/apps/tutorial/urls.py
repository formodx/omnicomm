from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import TutorialViewSet


router = SimpleRouter()
router.register('', TutorialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]