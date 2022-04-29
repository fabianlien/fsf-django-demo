from django.test import TestCase
from .forms import ItemForm


# Create your tests here.
class TestItemForm(TestCase):

    def test_name_field_required(self):
        form = ItemForm({'name': ''})
        self.assertTrue(form.is_valid() is False)
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_NOT_required(self):
        form = ItemForm({'name': 'Test'})
        self.assertTrue(form.is_valid())
