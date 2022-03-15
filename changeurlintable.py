from typing import List
import psycopg2
from psycopg2 import sql
import time
import os
import csv
import sys
csv.field_size_limit(sys.maxsize)
import yaml
import psycopg2.extras
from uuid import uuid4
import pandas as pd

URL = "localhost"
PORT = "5432"
VIOLATION_URL = f"http://{URL}:8050/get-files/"

try:
    connection = psycopg2.connect(user='postgres', password='SecuredPassword', host=URL, port=PORT, database="postgres")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    cursor = connection.cursor()
    query = f""" SELECT id,media_url FROM violations; """
    cursor.execute(query)
    records = cursor.fetchall()
    mydataframe = pd.DataFrame(records)
    connection.commit()
    connection.close()
except Exception as e:
    print(f'[Updating Violation Exception]: {e}')

def updatetheurl(id,url):
    try:
        connection = psycopg2.connect(user='postgres', password='SecuredPassword', host=URL, port=PORT, database="postgres")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cursor = connection.cursor()
        query = f""" UPDATE violations SET media_url = '{url}' WHERE id = '{id}'; """
        cursor.execute(query)
        connection.commit()
        connection.close()
    except Exception as e:
        print(f'[Updating Violation Exception]: {e}')


for i in range(len(mydataframe)):
    try:
        a = mydataframe[1][i].split('/get-files/')[0]
        b = mydataframe[1][i].split('/get-files/')[1]
        c = VIOLATION_URL + b
        updatetheurl(mydataframe[0][i],c)
        print(f"Done {i+1} out of {len(mydataframe)}")
    except Exception as e:
        print(f'[Updating Violation Exception]: {e}')

print("------------------------------------------------------")
try:
    connection = psycopg2.connect(user='postgres', password='SecuredPassword', host=URL, port=PORT, database="postgres")
    cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
    cursor = connection.cursor()
    query = f""" SELECT id,media_url FROM pdf_violations; """
    cursor.execute(query)
    records = cursor.fetchall()
    mypdfdataframe = pd.DataFrame(records)
    connection.commit()
    connection.close()
except Exception as e:
    print(f'[Updating Violation Exception]: {e}')

def updatethepdfurl(id,url):
    try:
        connection = psycopg2.connect(user='postgres', password='SecuredPassword', host=URL, port=PORT, database="postgres")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        cursor = connection.cursor()
        query = f""" UPDATE pdf_violations SET media_url = '{url}' WHERE id = '{id}'; """
        cursor.execute(query)
        connection.commit()
        connection.close()
    except Exception as e:
        print(f'[Updating Violation Exception]: {e}')

for i in range(len(mypdfdataframe)):
    a = mypdfdataframe[1][i].split('/get-files/')[0]
    b = mypdfdataframe[1][i].split('/get-files/')[1]
    c = VIOLATION_URL + b
    updatethepdfurl(mypdfdataframe[0][i],c)
    print(f"Done {i+1} out of {len(mypdfdataframe)}")
