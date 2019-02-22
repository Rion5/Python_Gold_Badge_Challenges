# Along with defining the proper class for a customer, your task will be to make 
# an application that allows administrators to do CRUD methods: create, read, update, and delete
# details about individual customers. 

# List View
# In addition to CRUD options, an administrator needs to show all customers order in a list like this:

# FirstName  LastName  Type        Email
# Jake        Smith     Potential   We currently have the lowest rates on Helicopter Insurance!
# James       Smith     Current     Thank you for your work with us. We appreciate your loyalty. Here's a coupon.
# Jane        Smith     Past        It's been a long time since we've heard from you, we want you back

# Be sure to Unit Test your Repository methods.
# Out of scope: Actually sending an email. We are just creating the string for the email.
# from challenge_5.customer_repository import CustomerRepository
from customer_repository import CustomerRepository
customer_repo = CustomerRepository([])


def print_menu_options():
    message = ("\nKomodo Insurance"
    "\n\t1) View all Customers"
    "\n\t2) Search for single Customers"
    "\n\t3) Add new Customer"
    "\n\t4) Update Customer"
    "\n\t5) Delete Customer"
    "\nPress any other key to exit()\n")
    user_input = input(message)
    return user_input

def menu_option_logic(user_option: str):
    if user_option == "1":
        customer_repo.view_all_customers()
        user_option = print_menu_options()
        menu_option_logic(user_option)
    elif user_option == "2":
        print("Search Customer")
        customer_to_search_first_name = input('Enter the first name of the Customer to view: ')
        customer_to_search_last_name = input('Enter the last name of the Customer to view: ')
        customer_repo.print_individual_customer_information(customer_to_search_first_name, customer_to_search_last_name)
        pass
    elif user_option == "3":
        print("Creating new Customer")
        customer_create_prompt()
    elif user_option == "4":
        print('Update Customer')
        customer_to_update_first_name = input('Enter the first name of the Customer you want to update: ')
        customer_to_update_last_name = input('Enter the last name of the Customer you want to update: ')
        customer_repo.update_customer(customer_to_update_first_name, customer_to_update_last_name)
    elif user_option == "5":
        print('Delete Customer')
        customer_to_delete_first_name = input('Enter the first name of the Customer you want to remove: ')
        customer_to_delete_last_name = input('Enter the last name of the Customer you want to remove: ')
        customer_repo.remove_customer(customer_to_delete_first_name, customer_to_delete_last_name)
    else:
        print('Exiting out of application')
        exit()

def customer_create_prompt():
    first_name      = input("Enter first name: ")
    last_name       = input("Enter last name: ")
    customer_type   = input("Enter customer type: ")
    email = customer_repo.assign_email_based_off_customer_type(customer_type)
    customer_repo.add_customer(first_name, last_name, customer_type, email)
    user_option = print_menu_options()
    menu_option_logic(user_option)

def customer_update_prompt():
    customer_to_update_first_name = input('Enter the first name of the Customer you want to update: ')
    customer_to_update_last_name = input('Enter the last name of the Customer you want to update: ')
    new_first_name = input('Enter the updated first name: ')
    new_last_name = input('Enter the updated last name: ')
    new_customer_type = input('Enter the updated Customer Type: ')
    new_customer_email = customer_repo.assign_email_based_off_customer_type(new_customer_type)
    customer_repo.update_customer(customer_to_update_first_name, customer_to_update_last_name)
    user_option = print_menu_options()
    menu_option_logic(user_option)

if __name__ == "__main__":
    customer_repo = CustomerRepository([])
    while True:
        user_option = print_menu_options()
        menu_option_logic(user_option)
# TODO: Could improve on the spacing, atm print statements are manually handled