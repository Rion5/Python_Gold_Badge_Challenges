import pytest
import unittest
# from challenge_5.customer_repository import CustomerRepository # if running from 'Python-104-GoldBadgeChallenges' directory
from customer_repository import CustomerRepository             # if running from inside 'challenge_5/' directory
# #python -m unittest test -v
class ChallengeFiveTests(unittest.TestCase):

    def setUp(self):
        self.customer_list = []
        self.customer_repo = CustomerRepository(self.customer_list)
        self.customer_repo.add_customer('John','Tester','Past', self.customer_repo.assign_email_based_off_customer_type('Past'))

    # Create Test
    def test_add_customer_should_add_1_customer_to_list(self):
        # Arrange - Done in the setUp() method
        # Act
        self.customer_repo.add_customer('Another','TestUser','Current', self.customer_repo.assign_email_based_off_customer_type('Current'))
        expected = 2
        actual = len(self.customer_repo.customer_list)
        # Assert
        self.assertEqual(expected, actual)

    # Update Test
    def test_update_customer_should_change_john_to_david(self):
        # Arrange - Done in the setUp() method
        # Act
        self.customer_repo.update_customer('John','Tester')
        # Assert - If the Update was successful, the Customer's name should be changed
        self.assertNotEqual('John', self.customer_list[0].first_name)

    # Delete Test
    def test_del_customer_should_remove_1_customer_from_list(self):
        # Arrange - Done in the setUp() method
        # Act
        self.customer_repo.remove_customer('John','Tester')
        expected = 0
        actual = len(self.customer_repo.customer_list)
        # Assert
        self.assertEqual(expected, actual)
    
    # Print Individual Test
    def test_print_individual_customer_should_print_information_for_john(self):
        # Arrange - Done in the setUp() method
        # Act
        self.customer_repo.print_individual_customer_information('John','Tester')
        expected = 1
        actual = len(self.customer_repo.customer_list)
        # Assert
        self.assertEqual(expected, actual)

    # View All Test
    def test_view_all_customers_should_print_1_customer(self):
        # Arrange - Done in the setUp() method
        # Act
        self.customer_repo.view_all_customers()
        expected = 1
        actual = len(self.customer_repo.customer_list)
        # Assert
        self.assertEqual(expected, actual)
    
    # Assign email logic Test
    def test_assign_email_logic_should_change_Customer_email_field(self):
        # Arrange - Done in the setUp() method
        # Act
        new_customer_type = 'Potential'
        self.customer_repo.customer_list[0].email = self.customer_repo.assign_email_based_off_customer_type(new_customer_type)
        expected = "We currently have the lowest rates on Helicopter Insurance!"
        actual = self.customer_repo.customer_list[0].email
        # Assert
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.customer_list.clear()
