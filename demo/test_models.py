from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):
    def test_done_default_is_False(self):
        item = Item.objects.create(name='test item')
        self.assertFalse(item.done)

    def test_str_method_returns_name(self):
        item = Item.objects.create(name='test')
        self.assertEqual(str(item), 'test')
