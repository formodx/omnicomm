from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import ChatViewSet


router = SimpleRouter()
router.register('chat', ChatViewSet)

urlpatterns = [
    path('', include(router.urls)),
]