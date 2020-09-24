from django.test import TestCase
from ponto.models import Ponto
from datetime import datetime


class TestModels(TestCase):
    def setUp(self):
        self.ponto = Ponto(
            data=datetime.today().date(),
            matricula="11",
            aves="Sim",
            foto="",
            latitude="21",
            longitude="22",
        )
        self.ponto.save()

    def test_str(self):
        self.assertEqual(self.ponto.__str__(), self.ponto.matricula)
