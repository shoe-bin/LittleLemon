from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
# from restaurant.models import Menu

class MenuViewTest(TestCase):

    def setup(self):
        self.item1 = Menu.objects.create(
            title = "Ice Cream",
            price = 7.00,
            inventory = 50
        )
        self.item2 = Menu.objects.create(
            title = "Salad",
            price = 15,
            inventory = 150
        )

    def test_getall(self):

        item = Menu.objects.create(
            title = "Salad",
            price = 15,
            inventory = 150
        )
        self.assertEqual(str(item), "Salad : 15")

