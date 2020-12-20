from django.test import TestCase
from .models import Article

# Create your tests here.
class ArticleTEst(TestCase):
    def setUp(self):
        Article.objects.create(title="Akun KU", content_text='ada kamu')
        print('sucess')
    def test_article_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(title="Akun KU")
        self.assertEqual(lion.title, 'The lion says "roar"')