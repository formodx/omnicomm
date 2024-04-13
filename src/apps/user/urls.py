from django.urls import path

from .views import GetUpdateAPIView
from .views import sign_in, sign_out
from .views import get_users, get_user_by_pk, change_password


urlpatterns = [
    path('', GetUpdateAPIView.as_view()),
    path('sign_in/', sign_in),
    path('sign_out/', sign_out),
    path('get_all/', get_users),
    path('get_by_pk/<int:pk>/', get_user_by_pk),
    path('change_password/', change_password),
]