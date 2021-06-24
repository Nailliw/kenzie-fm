from django.urls import path
from .views import UserView, LoginView, ProtectedCiew


urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/login/", LoginView.as_view()),
    path("users/protected/", ProtectedCiew.as_view()),
]
