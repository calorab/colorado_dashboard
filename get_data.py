import os
import snowflake.connector
import pandas as pd

'''Todo:
    1: rebuild county views using UNION so that I get one table for all counties
    2: rebuild Views Task in Snowflake
'''

# Set up connection to Snowflake
conn = snowflake.connector.connect(
    user='ETLPROG2023',
    password='NHqLFb2X6#CgoLtn',
    account='omb53008.us-east-1'
)

# Create a the snowflake cursor object
cur = conn.cursor()
# 
tables = ('DEMOGRAPHICS', 'HOUSING', 'PARKS_ADDRESS_API_DATA', 'PARKS_API_DATA', 'POI_INDEX_COMP', 'WEATHER_CLIMATE')

cur.execute('USE ROLE COL_ADMIN;')
cur.execute('USE DATABASE COLORADO;')
cur.execute('USE SCHEMA ANALYTICS;')
cur.execute('USE WAREHOUSE COL_WH;')


print(f'Before response from COUNTIES')
# execute statement
df = cur.execute('SELECT * FROM COLORADO.ANALYTICS.COUNTIES;').fetch_pandas_all()
print('Got the response')

# open dataFrame and write to a file data/<filename> probably just the table name
if not os.path.exists('data'):
    os.mkdir('data')
    print('Data directory created')

with open(os.path.join('data', 'counties'), 'w') as f:
    # write flat file data to this file
    df.to_csv(f, header=True, index=False)

    
for table in tables:
    # define select all statement and other vars
    file_name = table.lower()
    db_table = 'COLORADO.ANALYTICS.' + table
    query = f'SELECT * FROM {db_table};'
    location = os.path.join('data', file_name)
    print(f'Before response from {table}')
    # execute statement
    df = cur.execute(query).fetch_pandas_all()
    # open dataFrame and write to a file data/<filename> probably just the table name
    print('Got the response')

    if not os.path.exists('data'):
        os.mkdir('data')
        print('Data directory created')

    
    with open(location, 'w') as f:
        # write flat file data to this file
        df.to_csv(f, header=True, index=False)



cur.close()





