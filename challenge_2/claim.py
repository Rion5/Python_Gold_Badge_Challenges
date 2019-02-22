import datetime
class Claim:
    
    _id = 0

    def __init__(self, ClaimType: str, Description: str, ClaimAmount: float, DateOfAccident: datetime, DateOfClaim :datetime):
        self.id = Claim._id
        Claim._id += 1
        self.claim_type = ClaimType
        self.description = Description
        self.claim_amount = ClaimAmount
        self.date_of_accident = datetime.datetime.strptime(DateOfAccident, '%m/%d/%y')
        self.date_of_claim = datetime.datetime.strptime(DateOfClaim, '%m/%d/%y')
        self.is_valid = self.calculate_if_claim_is_valid()

    def calculate_if_claim_is_valid(self):
        time_between_claim_and_accident = self.date_of_accident.date() - self.date_of_claim.date()
        if abs(int(time_between_claim_and_accident.days)) <= 30:
            return True
        else:
            return False
