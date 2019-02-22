# from challenge_1.menu_repository import MenuRepository
from menu_repository import MenuRepository

# Run code below if running this file directly
if __name__ == "__main__":
    # List to hold Menu Item
    menu_list = []

    # Menu Repo
    menu_repo = MenuRepository(menu_list)
    menu_repo.print_menu_options()


