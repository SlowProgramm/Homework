from django.test import TestCase
from .models import Category, Author, Songs


class TestAnimalListView(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get('/songs/')

    def tearDown(self) -> None:
        pass

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_context(self):
        self.assertIn('help_text', self.response.context)
        self.assertEqual(self.response.context['help_text'], 'Помогающий текст')

    def test_animal_detail(self):
        response = self.client.get('/songs/999/')
        self.assertEqual(response.status_code, 404)

        category = Category.objects.create(title='Энергичная')
        author = Author.objects.create(username='Рамштаин')
        song = Songs.objects.create(name='Pop-Star', category=category, author=author)

        response = self.client.get(f'/songs/{song.pk}/')
        self.assertEqual(response.status_code, 200)
