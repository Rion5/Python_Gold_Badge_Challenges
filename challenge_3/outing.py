class Outing:
    _id = 0
    def __init__(self, event_type: str, num_people_attended: int, date: str, total_cost_per_person: float):
        self.id = Outing._id
        Outing._id += 1
        self.event_type = event_type
        self.num_people_attended = num_people_attended
        self.date = date
        self.total_cost_per_person = total_cost_per_person
        self.total_cost_of_event = self.calculate_cost_of_event()

    def calculate_cost_of_event(self):
        self.total_cost_of_event = int(self.num_people_attended) * float(self.total_cost_per_person)
        return self.total_cost_of_event

    def __repr__(self):
        return (
            f'Id: {self.id}\n'
            f'Event Type: {self.event_type}\n'
            f'# of people attended: {self.num_people_attended}\n'
            f'Date: {self.date}\n'
            f'Total cost per person: ${self.total_cost_per_person}\n'
            f'Total cost per event: ${self.total_cost_of_event}'
            )
