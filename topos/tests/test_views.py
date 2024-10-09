from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Topo

class TopoIntegrationTest(APITestCase):
    def setUp(self):
        self.topo = Topo.objects.create(nombre="Topo1", descripcion="Un topo", color="Gris", tamaño=12.5, fecha_encontrado="2023-01-01")

    def test_get_topo_list(self):
        url = reverse('topo-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_topo(self):
        url = reverse('topo-list-create')
        data = {'nombre': 'Topo2', 'descripcion': 'Otro topo', 'color': 'Marrón', 'tamaño': 10.0, 'fecha_encontrado': '2023-02-01'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

