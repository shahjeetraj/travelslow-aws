from django.test import TestCase
from .views import convert_m2h, entry

# Create your tests here.
class firstTestCase(TestCase):
    def test_convert(self):
        self.assertEqual(convert_m2h('CSS'),'<h1>CSS</h1>\n\n<p>CSS is a language that can be used to add style to an <a href="/wiki/HTML">HTML</a> page.</p>\n')
    
    def test_entry(self):
        self.assertEqual()
        self.assertTemplateUsed()