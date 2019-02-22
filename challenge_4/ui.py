from badge import Badge
from badge_repository import BadgeRepository
# from challenge_4.badge import Badge
# from challenge_4.badge_repository import BadgeRepository # For code completion
class UI:
    def __init__(self, badges_repository: BadgeRepository):
        self.badge_repo = badges_repository

    def print_menu_options_and_get_input(self):
        print("\nKomodo Insurance"
        "\n\t1) Add a Badge"
        "\n\t2) Edit a Badge"
        "\n\t3) List all Badges"
        "\nPress any other key to exit()")
        user_input = input('Select an option: ')
        return user_input

    def create_badge_prompt(self):
        badge_number  = input('What is the number on the badge: ')
        door_access_codes = self.add_door_access_prompt()
        new_badge = Badge(badge_number, door_access_codes)
        self.badge_repo.add_badge(new_badge)

    def add_door_access_prompt(self):
        door_access_codes = []
        result = True
        while result == True:
            user_input = input('List a door that needs access to: ')
            door_access_codes.append(user_input)
            add_another_door_access_code = input('Any other doors (y/n)? : ').lower()
            if add_another_door_access_code == "y":
                result = True
            else:
                result = False
        return door_access_codes

    def edit_badge_prompt(self):
        badge_number_to_edit = input('What is the badge number to update?: ')
        for i, badge in enumerate(self.badge_repo.badges_list):
            if badge.badge_number == badge_number_to_edit:
                print(f'\n{badge.badge_number} has access to doors {badge.list_of_door_names}')
                print('\nWhat would you like to do?')
                print('\t1. Remove a door')
                print('\t2. Add a door')
                user_input = input('Select an option: ')
                if user_input == "1":
                    access_code_to_remove = input('Which door access would you like to remove?: ')
                    self.badge_repo.remove_door(access_code_to_remove)
                elif user_input == "2":
                    access_code_to_add = input('Which door access would you like to add?: ')
                    self.badge_repo.add_door(badge.badge_number, access_code_to_add)
                else:
                    print('Error: Invalid Option')
                    self.edit_badge_prompt()
                
    def menu_option_logic(self, option_number: str):
        if option_number == "1":
            print('\nAdd a Badge')
            self.create_badge_prompt()
        elif option_number == "2":
            print('\nEdit a Badge')
            self.edit_badge_prompt()
        elif option_number == "3":
            print('\nList all Badges')
            self.badge_repo.view_all_badges()
        else:
            print('\nExiting out of application')
            exit()

if __name__ == "__main__":
    badge_repo = BadgeRepository([])
    ui = UI(badge_repo)
    while True:
        user_option = ui.print_menu_options_and_get_input()
        ui.menu_option_logic(user_option)
