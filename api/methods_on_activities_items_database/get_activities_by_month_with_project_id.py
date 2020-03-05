import datetime
import sqlite3
from datetime import datetime as dt

"""
* Documentation:
* ==============
*
* 1. Loop to get activities between the min_date and max_date
* ===========================================================
*
* First scenario: 08-2020 to 10-2020
** ====================================
** | looping | first date | last date |
** ------------------------------------
** |    1    |  08-2020   |  10-2020  |
** ====================================
*
* Second scenario: 08-2020 to 05-2021
** ====================================
** | looping | first date | last date |
** ------------------------------------
** |    1    |  08-2020   |  12-2020  |
** ------------------------------------
** |    2    |  01-2021   |  05-2021  |
** ====================================
*
* Third scenario: 08-2020 to 10-2022
** ====================================
** | looping | first date | last date |
** ------------------------------------
** |    1    |  08-2020   |  12-2020  |
** ------------------------------------
** |    2    |  01-2021   |  12-2021  |
** ------------------------------------
** |    2    |  01-2021   |  10-2021  |
** ====================================
*
* in range works like [ value1, value2 [
* so "diff_year + 1" because we need that for works when the counter comes to diff_year
* but diff_year is not includes => +1
*
"""


def run(project_id):
    conn = sqlite3.connect("../databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    # Get the min date of the activities in the project
    query = "SELECT min(date) FROM activities"
    min_date = cursor.execute(query).fetchone()[0]
    # Get the max date of the activities in the project
    query = "SELECT max(date) FROM activities"
    max_date = cursor.execute(query).fetchone()[0]
    # Format min_date and max_date
    date_min_datetime = dt.strptime(min_date, '%Y-%m-%d %H:%M:%S.%f')
    date_max_datetime = dt.strptime(max_date, '%Y-%m-%d %H:%M:%S.%f')
    # subtraction between max_date and min_date
    diff_year = date_max_datetime.year - date_min_datetime.year
    # Init array to get the total of activities in the month
    array = []
    # See documentation 1
    for cpt_year in range(diff_year + 1):
        # First month is 1
        min_cpt_month = 1
        # Last month is 12
        max_cpt_month = 12
        # If first time get in the for
        if cpt_year == 0:
            # Get min month
            min_cpt_month = date_min_datetime.month
        # If last time get in the for
        if cpt_year == diff_year:
            # get max month
            max_cpt_month = date_max_datetime.month
        # get current year with the counter
        year = date_min_datetime.year + cpt_year
        for cpt_month in range(min_cpt_month, max_cpt_month + 1):
            # First day is 1
            min_day = 1
            # Format the begin_date in date format
            date_start = dt.strptime(str(year) + "-" + str(cpt_month) + "-0" + str(min_day), '%Y-%m-%d')
            # get the last day of the month
            max_day = _last_day_of_month(date_start).day
            # Format the end_date in date format
            date_stop = dt.strptime(str(year) + "-" + str(cpt_month) + "-" + str(max_day) + " 23:59:59.999999",
                                    '%Y-%m-%d %H:%M:%S.%f')
            # get the total of activities by month of the project
            query = """SELECT count(*) FROM activities WHERE date BETWEEN  date(?) AND date(?)"""
            value = (date_start, date_stop)
            cursor.execute(query, value)
            # Push all the data in the array to return them
            array.append(cursor.fetchone()[0])
    return array


# Method to get the last day of a month
def _last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)
