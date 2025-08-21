from django.test import TestCase
from django.urls import reverse
from .models import Tarea

class TareasTests(TestCase):
    def test_lista_vacia_carga(self):
        resp = self.client.get(reverse("lista_tareas"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Sin tareas")

    def test_crear_tarea(self):
        Tarea.objects.create(titulo="Test", descripcion="Demo")
        resp = self.client.get(reverse("lista_tareas"))
        self.assertContains(resp, "Test")