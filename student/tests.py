from django.test import TestCase
from django.http import request
from .views import index

class TestView(TestCase):
    def test_index(self):
        # self.assertEquals request.get('http://localhost:8000').status_code == 200
        pass


if __name__ == '__main__':
    TestCase.run()