from django.contrib.auth.models import User
from django.test import TestCase

from .models import Equipment


class EquipmentModelTests(TestCase):
    def test_create_equipment(self):
        user = User.objects.create_user(username='testuser')
        device = Equipment.objects.create(
            owner=user,
            name='Router',
            mac_address='00:00:5e:00:53:af',
            ip_address='192.168.1.1',
        )
        self.assertEqual(device.owner, user)
        self.assertEqual(device.mac_address, '00:00:5e:00:53:af')
