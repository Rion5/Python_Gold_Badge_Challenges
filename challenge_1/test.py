
import pytest
import unittest
from menu_repository import MenuRepository
from menu import MenuItem
# from challenge_1 import cafe # To run if working from 'Python-104-GoldBadgeChallenges-master' directory
# Commands: 'python -m unittest challenge_1.test -v'

class ChallengeOneTests(unittest.TestCase):

    # setUp method is will run its code before every single test
    def setUp(self):
        self.menu_list = []
        self.menu_repo = MenuRepository(self.menu_list)
        self.menu_item = MenuItem(1, 'Burger', 9.99, 'Very delicious Burger',['Beef Patty', 'Cheese', 'Buns', 'Love'])
        self.menu_repo.add_menu_item(self.menu_item)

    # View All Test
    def test_view_all_menu_items_should_return_1_menu_item(self):
        # Arrange - setup variables
        #         - setup complete in setUp()
        # Act     - run test method
        expect = 1
        actual = len(self.menu_repo.menu_list)
        # Assert  - compare expected to actual results
        self.menu_item
        self.assertEqual(expect, actual)
    
    # Create Test
    def test_add_menu_item_should_add_1_menu_item(self):
        '''We start with 1 menu item in the list, after running method, the list should have 1 new menu item'''
        # Arrange
        # Act
        expect = 2
        new_menu_item = MenuItem(2, 'PB&J Sandwich', 3.99, 'Classic peanut butter and jelly sandwich',['Peanut Butter', 'Jelly', 'Bread'])
        self.menu_repo.add_menu_item(new_menu_item)
        actual = len(self.menu_repo.menu_list)
        # Assert
        self.assertEqual(expect, actual)

    # Delete Test
    def test_remove_menu_item_should_remove_1_menu_item(self):
        # Arrange
        # Act
        expect = 0
        self.menu_repo.remove_menu_item(1)
        actual = len(self.menu_repo.menu_list)
        # Assert
        self.assertEqual(expect, actual)
    
    # tearDown method will run after each test
    def tearDown(self):
        self.menu_list.clear

