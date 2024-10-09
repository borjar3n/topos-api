import time
from django.urls import reverse
from rest_framework.test import APITestCase

class TopoPerformanceTest(APITestCase):
    def test_topo_list_performance(self):
        start_time = time.time()
        response = self.client.get(reverse('topo-list-create'))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.assertLess(elapsed_time, 0.5)  # Asegúrate de que la respuesta tarde menos de 0.5 segundos

