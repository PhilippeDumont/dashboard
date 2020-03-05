import datetime
import sqlite3
from datetime import datetime as dt


def run(project_id):
    conn = sqlite3.connect("../databases_files/activities_items_db/" + str(project_id) + ".db")
    cursor = conn.cursor()
    query = "SELECT min(date) FROM activities"
    min_date = cursor.execute(query).fetchone()[0]
    query = "SELECT max(date) FROM activities"
    max_date = cursor.execute(query).fetchone()[0]
    date_min_datetime = dt.strptime(min_date, '%Y-%m-%d %H:%M:%S.%f')
    date_max_datetime = dt.strptime(max_date, '%Y-%m-%d %H:%M:%S.%f')
    diff_year = date_max_datetime.year - date_min_datetime.year
    array = []
    for cpt_year in range(diff_year + 1):
        min_cpt_month = 1
        max_cpt_month = 12
        if cpt_year == 0:
            min_cpt_month = date_min_datetime.month
        if cpt_year == diff_year:
            max_cpt_month = date_max_datetime.month
        year = date_min_datetime.year + cpt_year
        for cpt_month in range(min_cpt_month, max_cpt_month + 1):
            min_day = 1
            date_start = dt.strptime(str(year) + "-" + str(cpt_month) + "-0" + str(min_day), '%Y-%m-%d')
            max_day = _last_day_of_month(date_start).day
            date_stop = dt.strptime(str(year) + "-" + str(cpt_month) + "-" + str(max_day) + " 23:59:59.999999",
                                    '%Y-%m-%d %H:%M:%S.%f')
            query = """SELECT count(*) FROM activities WHERE date BETWEEN  date(?) AND date(?)"""
            value = (date_start, date_stop)
            cursor.execute(query, value)
            array.append(cursor.fetchone()[0])
    return array


def _last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)