from django.urls import path
from .views import TableListCreateView, TableDeleteView

urlpatterns = [
    path('', TableListCreateView.as_view(), name='table-list-create'),
    path('<int:pk>/', TableDeleteView.as_view(), name='table-delete'),
]
