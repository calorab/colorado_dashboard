import os
import snowflake.connector
import logging
from dotenv import load_dotenv

logging.basicConfig(filename='snowflake_data.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(message)s')
load_dotenv()

sf_password = os.getenv('SNOWFLAKE_PASSWORD')
sf_user = os.getenv('SNOWFLAKE_USER')
sf_account = os.getenv('SNOWFLAKE_ACCOUNT')

# Set up connection to Snowflake
conn = snowflake.connector.connect(
    user= sf_user,
    password= sf_password,
    account= sf_account
)

# Create the snowflake cursor object
cur = conn.cursor()
tables = ('DEMOGRAPHICS', 'HOUSING', 'PARKS_ADDRESS_API_DATA', 'PARKS_API_DATA', 'POI_INDEX_COMP', 'WEATHER_CLIMATE')

# Apply Role and Warehouse to queries
cur.execute('USE ROLE COL_ADMIN;')
cur.execute('USE DATABASE COLORADO;')
cur.execute('USE SCHEMA ANALYTICS;')
cur.execute('USE WAREHOUSE COL_WH;')

# execute statement
df = cur.execute('SELECT * FROM COLORADO.ANALYTICS.COUNTIES;').fetch_pandas_all()
logging.info('Got the response from Counties table')

# open dataFrame and write to a file data/<tablename> 
if not os.path.exists('data'):
    os.mkdir('data')
    logging.info('Data directory created')

with open(os.path.join('data', 'counties'), 'w') as f:
    # write flat file data to counties file
    df.to_csv(f, header=True, index=False)

    
for table in tables:
    # define select all statement and other vars
    file_name = table.lower()
    db_table = 'COLORADO.ANALYTICS.' + table
    query = f'SELECT * FROM {db_table};'
    location = os.path.join('data', file_name)
    
    # execute statement
    df = cur.execute(query).fetch_pandas_all()
    # open dataFrame and write to a file data/<filename> probably just the table name
    logging.info(f'Got the response from {table}')

    if not os.path.exists('data'):
        os.mkdir('data')
        logging.info('Data directory created')

    
    with open(location, 'w') as f:
        # write flat file data to this file
        df.to_csv(f, header=True, index=False)

logging.info('get_data.py completed successfully')
logging.info('Closing Snowflake connection')
cur.close()





