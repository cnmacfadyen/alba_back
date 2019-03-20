from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles import finders

# Create your tests here.

# Will  add more later

class GeneralTests(TestCase):
    def test_serving_static_files(self):
        result = finders.find('images/logo2.jpg')
        self.assertIsNotNone(result)


class IndexPageTests(TestCase):
        
    def test_index_contains_hello_message(self):
        response = self.client.get(reverse('index'))
        self.assertIn(b'Welcome!', response.content)
         
    def test_index_using_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'whiskyouaway/home.html')


class AboutPageTests(TestCase):
        
    def test_about_contains_create_message(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'Browse through our various events to view information', response.content)
        
        
    def test_about_contain_image(self):
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/', response.content)

    def test_about_using_template(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'whiskyouaway/about.html')
   