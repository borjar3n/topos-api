from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TopoSecurityTest(APITestCase):
    def test_post_without_required_fields(self):
        url = reverse('topo-list-create')
        data = {'nombre': ''}  # Falta información requerida
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

