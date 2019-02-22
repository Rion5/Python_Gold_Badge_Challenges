import pytest
import unittest
from claim import Claim
from claim_repository import ClaimRepository
# from challenge_2.claim import Claim
# from challenge_2.claim_repository import ClaimRepository

class ChallengeTwoTests(unittest.TestCase):

    def setUp(self):
        self.claim_repo = ClaimRepository([])
        self.claim = Claim('Car','Accident',350,'01/01/18','02/11/18')
        self.claim_repo.add_claim(self.claim)


    def test_add_claim_should_add_1_claim_to_list(self):
        # Arrange
        new_claim = Claim('Boat','Hijacked',555,'02/01/18','02/11/18')
        # Act
        self.claim_repo.add_claim(self.claim)
        expected = 2
        actual = len(self.claim_repo.claims_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_next_claim_should_remove_first_claim_in_list(self):
        # Arrange - done in setUp()
        # Act
        self.claim_repo.next_claim()
        expected = 0
        actual = len(self.claim_repo.claims_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_calculate_if_claim_is_valid_should_return_False(self):
        # Arrange - done in setUp()
        # Act
        expected = False
        actual = self.claim.is_valid
        # Assert
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.claim_repo.claims_list.clear()
