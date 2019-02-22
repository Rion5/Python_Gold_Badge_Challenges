from badge import Badge
# from challenge_4.badge import Badge
# from challenge_4.badge_repository import BadgeRepository
class BadgeRepository:
    def __init__(self, badges_list: list):
        self.badges_list = badges_list

    # Create
    def add_badge(self, badge: Badge):
        self.badges_list.append(badge)

    # View All
    def view_all_badges(self):
        print('Badge #\t\t\tDoor Access')
        for badge in self.badges_list:
            print(f'{badge.badge_number}\t\t', end = '\t')
            for door_access in badge.list_of_door_names:
                print(door_access, end = ' ')
            print()
