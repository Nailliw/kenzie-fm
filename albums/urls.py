from django.urls import path
from .views import (
    BandListCreateView,
    AlbumCreateView,
    TagCreateView,
    BandRetrieveUpdateView,
    BandMemberView,
)

urlpatterns = [
    path("bands/", BandListCreateView.as_view()),
    path("bands/<int:band_id>/", BandRetrieveUpdateView.as_view()),
    path("bands/<int:pk>/albums/", AlbumCreateView.as_view()),
    path("bands/<int:band_id>/tags/", TagCreateView.as_view()),
    path("bands/<int:band_id>/users/", BandMemberView.as_view()),
]
