import pandas as pd
from sqlalchemy import text

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:root@host.docker.internal/traffic_data')

VEHICLE_SCHEMA = "timed=vehicle_data_schema.sql"
TRAJECTORIES_SCHEMA = "trajectory_schema.sql"


def create_table():
    try:
        with engine.connect() as conn:
            for name in [VEHICLE_SCHEMA, TRAJECTORIES_SCHEMA]:
                with open(f'{name}') as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfull")
    except Exception as e:
        print(e)


# create_table()

def insert_table(df: pd.DataFrame, table_name: str ):
    try:
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn, if_exists='replace', index=False)
    except Exception as e:
        print(f"Failed  ---- {e}")  


