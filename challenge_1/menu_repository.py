from menu import MenuItem
class MenuRepository:
    def __init__(self, menu_list: list):
        self.menu_list = menu_list

    # Create
    def add_menu_item(self, menu_item: MenuItem):
        print(f'\n\tAdding {menu_item.meal_name} to the Menu')
        self.menu_list.append(menu_item)

    # Read
    def view_all_menu_item(self):
        print('\nView All Menu Items')
        if len(self.menu_list) == 0:
            print('There are no items on the Menu')
        else:
            for menu_item in self.menu_list:
                print(f'{menu_item.meal_number}: {menu_item.meal_name}\nPrice: ${menu_item.price}\nDescription: {menu_item.description}\nIngredients: {menu_item.ingredients}')

    # Delete
    def remove_menu_item(self, menu_item_meal_number: int):
        for menu_item in self.menu_list:
            if menu_item.meal_number == menu_item_meal_number:
                print(f"\n\tDeleting '{menu_item.meal_name}' from the menu")
                self.menu_list.remove(menu_item)

    # Print Menu, Take user's input, perform logic based on user's input
    def print_menu_options(self):
        print("\nKomodo Cafe Menu"
        "\n\t1) View all menu items"
        "\n\t2) Add new menu item"
        "\n\t3) Delete menu item"
        "\nPress any other key to exit()")
        user_input = input('Select an option: ')
        try:
            # Exit out of program, if input is not an int between 1-3
            value = int(user_input)
            if value < 1 or value > 3:
                raise ValueError
            if value == 1:
                # View all menu items
                self.view_all_menu_item()
                self.print_menu_options()
            if value == 2:
                # Prompt user to add a new menu item
                meal_number = input('Enter new meal number: ')
                meal_name   = input('Enter meal name: ')
                price       = input('Enter the price : $')
                description = input('Enter description: ')
                ingredients = input('Enter list of ingredients, separated by a blank space: ').split(' ')
                new_menu_item = MenuItem(meal_number, meal_name, price, description, ingredients)
                self.add_menu_item(new_menu_item)
                self.print_menu_options()
            if value == 3:
                # Delete menu item
                meal_number_to_delete = input('Enter the meal number you want to delete: ')
                self.remove_menu_item(meal_number_to_delete)
                self.print_menu_options()
        except ValueError:
            print('Exiting out of application')
            exit()