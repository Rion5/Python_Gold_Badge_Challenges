import pytest
import unittest
from badge import Badge
from badge_repository import BadgeRepository
# from challenge_4.badge import Badge
# from challenge_4.badge_repository import BadgeRepository
class ChallengeFourTests(unittest.TestCase):

    def setUp(self):
        self.badge_repo = BadgeRepository([])
        self.new_badge = Badge(1, ["a1", "a2"])
        self.badge_repo.badges_list.append(self.new_badge)

    def test_add_badge_should_add_1_item_to_list(self):
        # Arrange - done in setUp()
        new_badge = Badge(2, ["b1", "b2", "c1"])
        # Act
        self.badge_repo.badges_list.append(new_badge)
        expected = 2
        actual = len(self.badge_repo.badges_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_remove_door_from_badge_should_remove_1_access_code_from_badge(self):
        # Arrange - done in setUp()
        # Act
        self.badge_repo.remove_door_from_badge('a1')
        expected = 1
        actual = len(self.badge_repo.badges_list)
        # Assert
        self.assertEqual(expected, actual)

    def test_add_door_to_badge_should_add_1_access_code_to_badge(self):
        # Arrange - done in setUp()
        # # Act
        self.badge_repo.add_door_to_badge(1, 'a55')
        expected = 3
        actual = len(self.badge_repo.badges_list[0].list_of_door_names)
        # Assert
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.badge_repo.badges_list.clear()
