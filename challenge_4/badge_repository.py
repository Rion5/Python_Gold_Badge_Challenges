from badge import Badge
# from challenge_4.badge import Badge
class BadgeRepository:
    def __init__(self, badges_list: list):
        self.badges_list = badges_list

    # Create
    def add_badge(self, badge: Badge):
        self.badges_list.append(badge)

    # Remove Door from List
    def remove_door(self, access_code_to_remove):
        for i, badge in enumerate(self.badges_list):
            for j, access_code in enumerate(badge.list_of_door_names):
                if access_code == access_code_to_remove:
                    index_to_del = self.badges_list[i].list_of_door_names.index(self.badges_list[i].list_of_door_names[j])
                    # Remove the access door code from the list_of_door_names from inside the Badge class
                    self.badges_list[i].list_of_door_names.remove(self.badges_list[i].list_of_door_names[j])

    # Append Door to list
    def add_door(self, badge_number, new_access_code):
        # Append the access code to the correct badge
        for i, badge in enumerate(self.badges_list):
            if badge.badge_number == badge_number:
                self.badges_list[i].list_of_door_names.append(new_access_code)
                print('adding')
                return
    
    # View All
    def view_all_badges(self):
        print('Badge #\t\t\tDoor Access')
        for badge in self.badges_list:
            print(f'{badge.badge_number}\t\t', end = '\t')
            for door_access in badge.list_of_door_names:
                print(door_access, end = ' ')
            print()
