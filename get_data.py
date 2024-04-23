import os
import snowflake.connector 
import requests
import json
import pandas as pd

'''Create a script to get data from SF and write that data to files so that I don't have to connect to SF for every page or every dashboard visit'''

# Set up connection to Snowflake
conn = snowflake.connector.connect(
    user='ETLPROG2023',
    password='NHqLFb2X6#CgoLtn',
    account='omb53008.us-east-1'
)

# Create a the snowflake cursor object
cur = conn.cursor()

tables = ('DEMOGRAPHICS', 'HOUSING', 'PARKS_ADDRESS_API_DATA', 'PARKS_API_DATA', 'POI_INDEX', 'POI_INDEX_COMP', 'WEATHER_CLIMATE')
views = ('ADAMS_COUNTY', 'ARAPAHOE_COUNTY', 'BOULDER_COUNTY', 'DENVER_COUNTY', 'DOUGLAS_COUNTY', 'ELPASO_COUNTY', 'JEFFERSON_COUNTY', 'LARIMER_COUNTY', 'ZIP_COUNTY')

cur.execute('USE ROLE COL_ADMIN;')
cur.execute('USE DATABASE COLORADO;')
cur.execute('USE SCHEMA ANALYTICS;')
cur.execute('USE WAREHOUSE COL_WH;')

for table in tables:
    # define select all statement
    query = f'SELECT * FROM {table};'
    # execute statement
    response = cur.execute(query)
    # open dataFrame and write to a file data/<filename> probably just the table name 
    df = pd.DataFrame(response)
    pass

for view in views:
    # define select all statement

    # execute statement

    # open dataFrame and write to a file data/<filename> probably just the table name 
    pass







