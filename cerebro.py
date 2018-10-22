#! /usr/bin/env python3

import csv
from datetime import datetime

import parsedatetime
import psycopg2

conn = psycopg2.connect(
    dbname="postgres", user="postgres", host="localhost", port=5432)
cur = conn.cursor()


schema = """
CREATE TABLE aga_members (
    name text,
    id integer,
    chapter text,
    state text,
    rating numeric,
    sigma numeric,
    expiry date,
    updated date,
    mtype text
);
"""

cur.execute(schema)



def conv_dt(dt_string):
    cal = parsedatetime.Calendar()
    dt_obj, _ = cal.parseDT(datetimeString=dt_string)

    return dt_obj

def clean_null(val):
    clean_val = None
    if val != '':
        clean_val = val

    return clean_val


with open("tdlista.txt") as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        rd = dict(
            zip([
                "name",
                "id",
                "mtype",
                "rating",
                "expiry",
                "chapter",
                "state",
                "sigma",
                "updated",
            ], row))

        row_list = [
            clean_null(rd["name"]),
            clean_null(rd["id"]),
            clean_null(rd["chapter"]),
            clean_null(rd["state"]),
            clean_null(rd["rating"]),
            clean_null(rd["sigma"]),
            conv_dt(rd["expiry"]),
            conv_dt(rd["updated"]),
            clean_null(rd["mtype"]),
        ]

        cur.execute(
            f'INSERT INTO aga_members VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);',
            row_list)

conn.commit()
conn.close()
