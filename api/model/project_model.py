from datetime import date


class Project:
    id: int
    name: str
    creation_date: date
    last_opening_date: date
    nb_activities: int
    nb_items: int

    def __init__(self, id, name, creation_date, last_opening_date, nb_activities, nb_items):
        self.id = id
        self.name = name
        self.creation_date = creation_date
        self.last_opening_date = last_opening_date
        self.nb_activities = nb_activities
        self.nb_items = nb_items
