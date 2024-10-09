from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TopoFunctionalTest(APITestCase):
    def test_complete_flow(self):
        # Crear un topo
        create_url = reverse('topo-list-create')
        data = {'nombre': 'TopoFuncional', 'descripcion': 'Topo para prueba funcional', 'color': 'Negro', 'tamaño': 9.0, 'fecha_encontrado': '2023-03-01'}
        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Listar topos
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

