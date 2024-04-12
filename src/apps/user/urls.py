from django.urls import path

from .views import GetUpdateAPIView
from .views import ChangePasswordAPIView
from .views import sign_in
from .views import sign_out
from .views import get_users
from .views import get_user_by_pk


urlpatterns = [
    path('', GetUpdateAPIView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('sign_in/', sign_in),
    path('sign_out/', sign_out),
    path('get_all/', get_users),
    path('get_by_pk/<int:pk>/', get_user_by_pk),
]