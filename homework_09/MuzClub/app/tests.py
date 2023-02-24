from django.test import TestCase
from .views import random_rating
from .models import Category, Author, Songs


class TestCategory(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(title='Грустная')

    def tearDown(self) -> None:
        self.category.delete()

    def test_init(self):
        self.assertTrue(isinstance(self.category.title, str))
        self.assertEqual(self.category.title, 'Грустная')

    def test_str(self):
        category = Category.objects.get(title='Грустная')
        self.assertEqual(str(category), 'Грустная')


class TestAuthor(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(username='Артур Пирожков')

    def tearDown(self) -> None:
        self.author.delete()

    def test_init(self):
        self.assertTrue(isinstance(self.author.username, str))
        self.assertEqual(self.author.username, 'Артур Пирожков')

    def test_str(self):
        author = self.author
        self.assertEqual(str(author), 'Артур Пирожков')


class TestSong(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(title='Энергичная')
        self.author = Author.objects.create(username='Артур Пирожков')
        self.rating = random_rating()
        self.song = Songs.objects.create(name='Рассвет', category=self.category, author=self.author, rating=self.rating)

    def tearDown(self) -> None:
        self.song.delete()
        self.category.delete()
        self.author.delete()

    def test_init(self):
        self.assertTrue(isinstance(self.author.username, str))
        self.assertEqual(self.author.username, 'Артур Пирожков')

    def test_str(self):
        self.assertEqual(str(self.song), f"Рассвет [Энергичная] [Артур Пирожков] [{self.rating}]")


class TestContext(TestCase):
    def test_context(self):
        response = self.client.get('/songs/')
        self.assertIn('help_text', response.context)
        self.assertEqual(response.context['help_text'], 'Помогающий текст')
