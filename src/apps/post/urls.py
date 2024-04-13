from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import PostViewSet


router = SimpleRouter()
router.register('', PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]