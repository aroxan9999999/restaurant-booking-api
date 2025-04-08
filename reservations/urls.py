from django.urls import path
from .views import ReservationListCreateView, ReservationDeleteView

urlpatterns = [
    path('', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationDeleteView.as_view(), name='reservation-delete'),
]
