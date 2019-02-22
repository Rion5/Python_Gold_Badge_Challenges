# Badge Class
# Fields: Id, List of Door names for access
class Badge:
     _id = 0
     
     def __init__(self, badge_number, list_of_door_access_names: list):
        self._id = Badge._id
        Badge._id += 1
        self.badge_number = badge_number
        self.list_of_door_names = list_of_door_access_names
        