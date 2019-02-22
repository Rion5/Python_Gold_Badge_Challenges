import pytest
import unittest
from outing import Outing
from outing_repository import OutingRepository
# python -m unittest test -v
# from challenge_3.outing import Outing
# from challenge_3.outing_repository import OutingRepository
class ChallengeThreeTests(unittest.TestCase):

    def setUp(self):
        self.outing_list = []
        self.outing_repo =OutingRepository(self.outing_list)
        new_outing = Outing('golf',10,'01/01/2019',10)
        self.outing_repo.add_outing(new_outing)

    # Create Test
    def test_add_outing_should_add_1_outing_to_list(self):
        # Arrange
        new_outing = Outing('bowling',13,'02/02/2019',5)
        # Act
        self.outing_repo.add_outing(new_outing)
        expected = 2
        actual = len(self.outing_list)
        # Assert
        self.assertEqual(expected, actual)
    
    # Read Test
    def test_view_all_outings(self):
        # Arrange - Done in the setUp() method
        # Act
        self.outing_repo.view_all_outings()
        expected = 1
        actual = len(self.outing_list)
        # Assert
        self.assertEqual(expected, actual)
    
    # Calculate costs for all outings Test
    def test_calculate_sum_cost_of_all_outings(self):
        # Arrange - Done in the setUp() method
        # Act
        expected = 100
        actual = self.outing_repo.calculate_sum_cost_of_all_outings()
        # Assert
        self.assertEqual(expected, actual)
    
    # Calculate costs for all 'bowling' outings Test
    def test_calculate_sum_cost_of_outing_event_type(self):
        # Arrange - Done in the setUp() method
        new_outing = Outing('bowling',5,'01/01/2019',7)
        # Act
        self.outing_repo.add_outing(new_outing)
        expected = 35
        actual = self.outing_repo.calculate_sum_cost_of_outing_event_type('bowling')
        # Assert
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.outing_list.clear()
