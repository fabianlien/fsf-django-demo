from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add_item')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_edit_item_page(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        response = self.client.post('/add_item', {'name': 'Test task'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test todo item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        self.assertFalse(Item.objects.get(id=item.id).done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test todo item', done=True)
        response = self.client.post(f'/edit/{item.id}', {'name': 'updated item'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertNotEqual(item.name, updated_item.name)

