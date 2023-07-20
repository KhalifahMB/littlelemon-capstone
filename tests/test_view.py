from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu model
        Menu.objects.create(title='Item 1', price=10, inventory=100)
        Menu.objects.create(title='Item 2', price=15, inventory=150)
        Menu.objects.create(title='Item 3', price=20, inventory=200)

        self.client = APIClient()

    def test_getall(self):
        # Retrieve all Menu objects from the API
        # Replace with your actual API endpoint URL
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')

        # Check if the request was successful (status code 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()

        # Serialize the database queryset
        serializer = MenuSerializer(menus, many=True)

        # Compare the serialized data with the response data
        self.assertEqual(response.data, serializer.data)
