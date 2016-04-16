from datetime import datetime

from django.test import TestCase
from effectiveworkout.monthlyplans.models import PlanoMensalidade


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.obj = PlanoMensalidade(
            nome='WK Rapidinha',
            valor=15.00,
            horario='Tarde',
            ativo=True
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(PlanoMensalidade.objects.exists())

    def test_created_at(self):
        """PlanoMensalidade must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('WK Rapidinha', str(self.obj.nome))
