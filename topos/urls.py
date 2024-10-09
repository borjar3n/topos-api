from django.urls import path
from . import views

urlpatterns = [
    path('topos/', views.TopoListCreateView.as_view(), name='topo-list-create'),
    path('topos/<int:pk>/', views.TopoDetailView.as_view(), name='topo-detail'),
]

