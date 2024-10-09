from django.urls import path
from .views import TopoListCreate, TopoRetrieveUpdateDelete

urlpatterns = [
    path('topos/', TopoListCreate.as_view(), name='topo-list-create'),
    path('topos/<int:pk>/', TopoRetrieveUpdateDelete.as_view(), name='topo-retrieve-update-delete'),
]

