from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import MessageViewSet


router = SimpleRouter()
router.register('message', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]