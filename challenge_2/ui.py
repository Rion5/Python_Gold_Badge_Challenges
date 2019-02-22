# import datetime
from claim import Claim
from claim_repository import ClaimRepository
# UI Menu
claim_repo = ClaimRepository([])
def print_menu_options_and_get_input():
    print("\nKomodo Claims Department"
    "\n\t1) See all Claims"
    "\n\t2) Take care of next Claim"
    "\n\t3) Enter a new Claim"
    "\nPress any other key to exit()")
    user_input = input('Select an option: ')
    return user_input
def create_new_claim_prompt():
    claim_type          = input('Enter Claim Type: ')
    description         = input('Enter claim description: ')
    claim_amount        = input('Enter claim amount: $')
    date_of_accident    = input('Enter date of accident (mm/dd/yy): ')
    date_of_claim       = input('Enter date of claim    (mm/dd/yy): ')
    new_claim = Claim(claim_type, description, claim_amount, date_of_accident, date_of_claim)
    return new_claim
def take_care_of_claim_prompt():
    for claim in claim_repo.claims_list:
        print(
            f'\nClaimId         : {claim.id}'
            f'\nType            : {claim.claim_type}'
            f'\nDescription     : {claim.description}'
            f'\nAmount          : {claim.claim_amount}'
            f'\nDate of Accident: {claim.date_of_accident}'
            f'\nDate of Claim   : {claim.date_of_claim}'
            f'\nIs Valid?       : {claim.is_valid}'
        )
        user_input = input('Do you want to deal with this claim now (y/n)? : ').lower()
        if user_input == "y":
            claim_repo.next_claim()
            take_care_of_claim_prompt()
        elif user_input == "n":
            return
        else:
            print("Error: Invalid option")
            return
def menu_option_logic(option_number: str):
    if option_number == "1":
        print('\nSee all claims')
        claim_repo.view_all_claims()
    elif option_number == "2":
        print('\nTake care of next Claim')
        take_care_of_claim_prompt()
    elif option_number == "3":
        print('\nEnter a new Claim')
        new_claim = create_new_claim_prompt()
        claim_repo.add_claim(new_claim)
    else:
        print('\nExiting out of application')
        exit()

if __name__ == "__main__":
    claim = Claim('Car','Accident',350,'01/01/18','02/01/18')
    claim2 = Claim('Boat','Hijacking',450,'02/01/18','02/01/18')
    claim_repo.add_claim(claim)
    claim_repo.add_claim(claim2)
    while True:
        user_input = print_menu_options_and_get_input()
        menu_option_logic(user_input)
        # break

# Start of test
claim = Claim('Car','Accident',350,'01/01/18','02/01/18')
print(f'{claim.date_of_accident.date()} - {claim.date_of_claim.date()}')
time_between_claim_and_accident = claim.date_of_accident.date() - claim.date_of_claim.date()
print(type(time_between_claim_and_accident))
print(time_between_claim_and_accident)
print(abs(time_between_claim_and_accident.days))
claim.calculate_if_claim_is_valid()

claim_repo.add_claim(claim)
claim_repo.view_all_claims()
# end of Test