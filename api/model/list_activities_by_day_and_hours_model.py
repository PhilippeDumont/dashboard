from model.list_day import ListDay


class ListActivitiesByDayAndHours:
    list_all_days = list()

    def __init__(self):
        for cpt in range(7):
            self.list_all_days.append(ListDay())
