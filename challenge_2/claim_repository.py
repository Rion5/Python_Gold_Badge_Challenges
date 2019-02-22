import claim
# from challenge_2.claim import Claim

class ClaimRepository:
    def __init__(self, claims_list: list):
        self.claims_list = claims_list

    # Create
    def add_claim(self, claim: claim.Claim):
        self.claims_list.append(claim)
    
    # Read
    def view_all_claims(self):
        print('Id\tType\tDescription\tAmount\tDOA\t\tDOC\t\tIsValid')
        for claim in self.claims_list:
            print(
                f'{claim.id}\t{claim.claim_type}\t{claim.description}\t${claim.claim_amount}\t{claim.date_of_accident.date()}\t{claim.date_of_claim.date()}\t{claim.is_valid}'
            )

    # Take care of next claim
    def next_claim(self):
        for claim in range(len(self.claims_list)):
            return self.claims_list.pop(claim)
