from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from effectiveworkout.usersprofiles.models import UserProfile


class UserProfileModelTest(TestCase):
    def setUp(self):
        self.obj = User(
            pk=1,
            username='admin',
            first_name='admin',
            last_name='admin',
            email='admim@admin.com',
            password='admin'
        )

        self.obj.save()

        self.obj1 = UserProfile(
            user_id=1,
            planomensalidade_id=1,
            datainicio='2016-01-20',
            datanascimento='2016-01-20',
            idade='42',
            cc='123456',
            nif='123456',
            telefone='9660608545',
            telefone2='9660608545',
            ativo=True
        )

        self.obj1.save()

    def test_create(self):
        self.assertTrue(UserProfile.objects.exists())

    def test_created_at(self):
        """UserProfile must have an auto created_at attr."""
        self.assertIsInstance(self.obj1.created_at, datetime)

    def test_str(self):
        self.assertEqual('admin', str(self.obj.first_name))
