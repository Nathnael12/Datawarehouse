import pandas as pd
from sqlalchemy import text
import json
from sqlalchemy import create_engine
import numpy as np

engine = create_engine('postgresql+psycopg2://postgres:root@host.docker.internal/traffic_data')

VEHICLE_SCHEMA = "timed_vehicle_data_schema.sql"
TRAJECTORIES_SCHEMA = "trajectory_schema.sql"


def create_table():
    try:
        with engine.connect() as conn:
            for name in [TRAJECTORIES_SCHEMA,VEHICLE_SCHEMA]:
                
                with open(f'/opt/pgsql/{name}', "r") as file:
                    query = text(file.read())
                    conn.execute(query)
        print("Successfull")
    except Exception as e:
        print("Error creating table",e)


# create_table()

def insert_to_table(json_stream :str, table_name: str,from_file=False ):
    try:
        if not from_file:
            df = pd.read_json(json_stream)
        else:
            # df = pd.read_json(f'../temp/{json_stream}')
            with open(f'../temp_storage/{json_stream}','r') as file:
                data=file.readlines()
            dt=data[0]

            df=pd.DataFrame.from_dict(json.loads(dt))
            df.columns=df.columns.str.replace(' ','')

            # TODO: This(the following line) shall be fixed when using cloud services
            # due to local memory (resource) shortage, I minimized the df to be loaded, 
            df=df.loc[:np.floor(df.shape[0]/2),:] 
            df.dropna(inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

    except Exception as e:
        print(f"error insert to table: {e}")  


