from django.urls import path
from .views import ShowView

urlpatterns = [
    path(
        "bands/<int:band_id>/shows/",
        ShowView.as_view(),
    )
]
