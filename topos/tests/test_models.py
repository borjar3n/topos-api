from django.test import TestCase
from ..models import Topo

class TopoModelTest(TestCase):
    def setUp(self):
        self.topo = Topo.objects.create(
            nombre="Topo1", descripcion="Este es un topo", color="Gris", tamaño=12.5, fecha_encontrado="2023-01-01"
        )

    def test_topo_creation(self):
        self.assertEqual(self.topo.nombre, "Topo1")

