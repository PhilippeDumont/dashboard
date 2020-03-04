import sqlite3
from datetime import datetime
import math

from model.list_activities_by_day_and_hours_model import ListActivitiesByDayAndHours


def get_activities_for_hours_in_week_by_day_by_project_id(project_id, date_debut, date_fin):
    date_debut_datetime = datetime.strptime(date_debut, '%Y-%m-%d')
    date_fin_datetime = datetime.strptime(date_fin, '%Y-%m-%d')
    starting_day = date_debut_datetime.weekday()
    ending_day = date_fin_datetime.weekday()
    differences_day = abs((date_fin_datetime - date_debut_datetime).days)
    nb_week = math.ceil((differences_day/7))
    conn = sqlite3.connect("api/databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    list_activities_by_day_and_hours = ListActivitiesByDayAndHours()   ## Init all the list containing all of the hours

    for cpt_days in range(7):                #### Seven days of the week
        for cpt_hours in range(24):
            for cpt_sem in range(nb_week):
                if nb_week == 0 and starting_day > cpt_days:
                    pass                            ## Pass if the first day isn't a Monday
                elif (nb_week - 1) == cpt_sem and ending_day < cpt_days:
                    break                           ## Stop after the last day necessary
                else:
                    query = """SELECT count(*) from """
                    list_activities_by_day_and_hours.list_all_days.index(cpt_days)[cpt_hours] = \
                        list_activities_by_day_and_hours.list_all_days.index(cpt_days)[cpt_hours] + nb_act_hours
