import pandas as pd
from sqlalchemy import create_engine
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data/supply_chain_data.csv")

supply_chain_df = pd.read_csv(DATA_DIR)

# PostgreSQL connection string
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = 'localhost' 
USER = 'postgres'
PASSWORD = 'admin'
PORT = 5432
DATABASE = 'supply_chain'

# Create SQLAlchemy engine
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')

# Convert DataFrame to SQL
supply_chain_df.to_sql('supply_chain_data', engine, if_exists = 'append', index = False)

print("DataFrame has been written to the SQL database.")