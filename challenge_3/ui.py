#   Komodo Outings
# Komodo accountants need a list of all outings, the cost of all outings combined, and the
# cost of all types of outings combined.
# Here are the parts of an outing:
# 	Event Type:
# 		Golf, Bowling, Amusement Park, Concert
# 	Number of people that attended,
# 	Date,
# 	Total cost per person for the event,
# 	Total cost for the event

# Here's what they'd like:
# 1. Display a list of all outings.
# 2. Add individual outings to a list(don't need to worry about delete yet)
# 3. Calculations:
# 	They'd like to see a display for the combined cost for all outings.
# 	They'd like to see a display of outing costs by type.
# 		For example, all bowling outings for the year were $2000.00.
# 		All Concert outings cost $5000.00.
# Be sure to Unit Test your Repository methods.
from outing import Outing
from outing_repository import OutingRepository

# use this to get vscode completion
# from challenge_3.outing_repository import OutingRepository 
outing_repo = OutingRepository([])

def print_menu_options_and_get_input():
    print("\nKomodo Outings"
    "\n\t1) View all Outings"
    "\n\t2) Add new Outing"
    "\n\t3) View combined cost for all Outings"
    "\n\t4) View combined cost for Outings based off type"
    "\nPress any other key to exit()")
    user_input = input('Select an option: ')
    return user_input

def menu_option_logic(user_option: str):
    if user_option == "1":
        print('\nView all Outings')
        outing_repo.view_all_outings()
    elif user_option == "2":
        print('\nAdd new Outing')
        new_outing = create_new_outing_prompt()
        outing_repo.add_outing(new_outing)
    elif user_option == "3":
        print('\nView combined cost for all Outings')
        sum = outing_repo.calculate_sum_cost_of_all_outings()
        print(f'Cost of all Outings: ${sum}')
    elif user_option == "4":
        print('\nView combined cost for Outings based off type')
        event_type = input('Enter event type: ')
        sum = outing_repo.calculate_sum_cost_of_outing_event_type(event_type)
        print(f'Cost of all {event_type} Outings: ${sum}')
    else:
        print('\nExiting out of application')
        exit()

# Ask user to fill fields for a new Outing
def create_new_outing_prompt():
    event_type              = input('Enter Event Type: ')
    num_people_attended     = input('Enter # of people attended: ')
    date                    = input('Enter date : ')
    total_cost_per_person   = input('Enter price per person: $')
    new_outing = Outing(event_type, num_people_attended, date, total_cost_per_person)
    return new_outing
if __name__ == "__main__":
    # print_menu_options_and_get_input()
    # # Outing Repo    
    # outing_repo = OutingRepository([])
    # # Create new Outing
    # outing1 = Outing('Golf',10, '01/01/2019',100)
    # # Add Outing to list
    # outing_repo.add_outing(outing1)
    # # print(outing1.total_cost_per_person)
    # print(f"Outing's total cost of event: ${outing1.total_cost_of_event}")
    # print(len(outing_repo.outing_list))
    # outing_repo

    while True:
        user_option = print_menu_options_and_get_input()
        menu_option_logic(user_option)