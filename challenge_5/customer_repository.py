# from challenge_5.customer import Customer
from customer import Customer

class CustomerRepository:
    def __init__(self, customer_list: list):
        self.customer_list = customer_list

    # Create
    def add_customer(self, first_name: str, last_name: str, customer_type: str, email: str):
        new_customer = Customer(first_name, last_name, customer_type, email)
        self.customer_list.append(new_customer)
    
    # Read
    def print_individual_customer_information(self, first_name: str, last_name: str):
        # find customer with matching first name and last name
        customer = [x for x in self.customer_list if x.first_name == first_name and x.last_name == last_name]
        print(f'\nName : {customer[0].first_name} {customer[0].last_name}\nType : {customer[0].customer_type}\nEmail: {customer[0].email}')
    
    # Update
    def update_customer(self, customer_to_update_first_name, customer_to_update_last_name):
        new_first_name = input('Enter the updated first name: ')
        new_last_name = input('Enter the updated last name: ')
        new_customer_type = input('Enter the updated Customer Type: ')
        new_customer_email = self.assign_email_based_off_customer_type(new_customer_type)
        # Delete and Add
        self.remove_customer(customer_to_update_first_name, customer_to_update_last_name)
        self.add_customer(new_first_name, new_last_name, new_customer_type, new_customer_email)
    
    # Delete
    def remove_customer(self, customer_to_delete_first_name, customer_to_delete_last_name):
        # Delete Customer from self.customer_list
        print(customer_to_delete_first_name)
        print(customer_to_delete_last_name)
        customer = [x for x in self.customer_list if x.first_name == customer_to_delete_first_name and x.last_name == customer_to_delete_last_name]
        self.customer_list.remove(customer[0])
        print('Removed Customer')
    
    # View All
    def view_all_customers(self):
        print(f'\nFirstName\t\tLastName\t\tType\t\tEmail')
        for customer in self.customer_list:
            if len(customer.last_name) < 8:
                print(f'{customer.first_name}\t\t\t{customer.last_name}\t\t\t{customer.customer_type}\t{customer.email}')
            else:
                print(f'{customer.first_name}\t\t\t{customer.last_name}\t\t{customer.customer_type}\t\t{customer.email}')

    # Assign email logic
    def assign_email_based_off_customer_type(self, customer_type: str):
        if customer_type == "Past":
            past_customer_string = "It's been a long time since we've heard from you, we want you back"
            return past_customer_string
        elif customer_type == "Current":
            current_customer_string = "Thank you for your work with us. We appreciate your loyalty. Here's a coupon."
            return current_customer_string
        elif customer_type == "Potential":
            potential_customer_string = "We currently have the lowest rates on Helicopter Insurance!"
            return potential_customer_string
        else:
            print("Invalid Customer Type (Must be Past, Current, or Potential\nDefault setting to 'Potential'")
            potential_customer_string = "We currently have the lowest rates on Helicopter Insurance!"
            return potential_customer_string

#TODO: Extract print statements to the ui