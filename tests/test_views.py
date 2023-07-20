# from django.test import TestCase
# from restaurant.models import Menu

# class MenuViewTest(TestCase):
#     def setUp(self):
#         # menu = Menu.
#         return super().setUp()
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Menu, Booking
from restaurant.serializers import MenuSerializer, UserSerializer, BookingSerializer

class MenuViewsTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test menu items
        self.menu_item_1 = Menu.objects.create(title='Item1', price=10, inventory=100)
        self.menu_item_2 = Menu.objects.create(title='Item2', price=15, inventory=150)

    def test_menu_items_list(self):
        url = '/menu/'  # Replace this with the actual URL for your MenuItemsView
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuSerializer([self.menu_item_1, self.menu_item_2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_single_menu_item_retrieve(self):
        url = f'/menu/{self.menu_item_1.pk}/'  # Replace this with the actual URL pattern for SingleMenuItemView
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = MenuSerializer(self.menu_item_1).data
        self.assertEqual(response.data, expected_data)

    def test_single_menu_item_update(self):
        url = f'/menu/{self.menu_item_1.pk}/'  # Replace this with the actual URL pattern for SingleMenuItemView
        data = {'title': 'New Item Name', 'price': 20, 'inventory': 50}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu_item_1.refresh_from_db()
        self.assertEqual(self.menu_item_1.title, data['title'])
        self.assertEqual(self.menu_item_1.price, data['price'])
        self.assertEqual(self.menu_item_1.inventory, data['inventory'])

    def test_single_menu_item_delete(self):
        url = f'/menu/{self.menu_item_1.pk}/'  # Replace this with the actual URL pattern for SingleMenuItemView
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Menu.objects.filter(pk=self.menu_item_1.pk).exists())

class BookingViewsTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        # Create test bookings
        self.booking_1 = Booking.objects.create(user=self.user, date='2023-07-19', time='12:00')
        self.booking_2 = Booking.objects.create(user=self.user, date='2023-07-20', time='15:30')

    def test_booking_list(self):
        url = '/bookings/'  # Replace this with the actual URL pattern for your BookingViewSet
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = BookingSerializer([self.booking_1, self.booking_2], many=True).data
        self.assertEqual(response.data, expected_data)

    # Add more tests for retrieve, create, update, and delete operations for BookingViewSet if needed

