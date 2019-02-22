# from challenge_3.outing import Outing
from outing import Outing

class OutingRepository:
    def __init__(self, outing_list: list):
        self.outing_list = outing_list
    
    # Create
    def add_outing(self, outing: Outing):
        self.outing_list.append(outing)

    # Read
    def view_all_outings(self):
        for outing in self.outing_list:
            print(
            f'\nId: {outing.id}\n'
            f'Event Type: {outing.event_type}\n'
            f'# of people attended: {outing.num_people_attended}\n'
            f'Date: {outing.date}\n'
            f'Total cost per person: ${outing.total_cost_per_person}\n'
            f'Total cost per event: ${outing.total_cost_of_event}')

    # Calculate costs for all Outings Test
    def calculate_sum_cost_of_all_outings(self):
        sum = 0
        for outing in self.outing_list:
            sum += float(outing.total_cost_of_event)
        return sum
    
    # View Combined cost for Outings based off event_type
    def calculate_sum_cost_of_outing_event_type(self, event_type):
        filtered_list = [x for x in self.outing_list if x.event_type == event_type]
        sum = 0
        for outing in filtered_list:
            sum += float(outing.total_cost_of_event)
        return sum