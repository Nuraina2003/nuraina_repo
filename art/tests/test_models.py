from django.urls import resolve

from django.test import TestCase
from ..models import *


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method:test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)


    def test_model_str(self):
        name = Category.objects.create(name='Django Testing')
        self.assertEqual(str(name), 'Django Testing')

    def test_get_register_is_resolved(self):
        url = reverse('register')
        print(resolve(url).func)
        #self.assertEqual(resolve(url))


class URLTests(TestCase):
    def test_testartHomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)