import pandas as pd
from logger import Logger
import sys
class DataLoader():
    
    def __init__(self)->None:
        self.logger=Logger().get_app_logger()
        self.logger.info('Data loader object Initialized')
    
    def get_columns_and_rows(self,file_path)->tuple:
        try:
            with open(f'../data/{file_path}','r') as f:
                lines=f.readlines()

            columns=lines[0].replace('\n','').split(';')
            data=lines[1:]
            return columns,data
        except Exception as e:
            self.logger.error(f"Failed to read data: {e}")
            sys.exit(1)
    
    def chunk_list(self,list,chunk_size,default_first_val=None)->list:
        chunked_list=[]
        for i in range(0, len(list), chunk_size):
            if default_first_val:
                values=[default_first_val]
                values.extend(list[i:i+chunk_size])
                chunked_list.append(values)
            else:
                chunked_list.append(list[i:i+chunk_size])

        return chunked_list

    def prepare_data_for_pandas(self,columns,all_data)->tuple:
        try:
            trajectory_cols=columns[:4]
            trajectory_rows=[]

            timed_vehicle_cols=['track_id']+columns[4:]
            timed_vehicle_rows=[]

            for row in all_data:
                try:
                    items=row.replace('\n','').split(';')
                    trajectory_rows.append(items[:4])
                    timed_vehicle_rows.extend(self.chunk_list(items[4:],6,items[0]))
                except Exception as e:
                    self.logger.error(f"Failed preparing data for pands at row {row}: {e}")
            
            return (trajectory_cols,trajectory_rows),(timed_vehicle_cols,timed_vehicle_rows)
        except Exception as e:
            self.logger.error(f"Failed to prepare data for pandas: {e}")
    
    def prepare_data_frame(self,trajectory_data:tuple,timed_vehicle_data:tuple)->tuple[pd.DataFrame,pd.DataFrame]:

        try:
            trajectory_cols,trajectory_rows=trajectory_data
            timed_vehicle_cols,timed_vehicle_rows=timed_vehicle_data

            trajectory_data=pd.DataFrame(columns=trajectory_cols,data=trajectory_rows)
            timed_vehicle_data=pd.DataFrame(columns=timed_vehicle_cols,data=timed_vehicle_rows)

            return trajectory_data,timed_vehicle_data

        except Exception as e:
            self.logger.error(f"Failed to prepare data frame: {e}")

    def extract_data(self,file_path:str)->pd.DataFrame:
        try:
            columns,all_data=self.get_columns_and_rows(file_path=file_path)
            trajectory_data, timed_vehicle_data=self.prepare_data_for_pandas(columns=columns,all_data=all_data)
            return self.prepare_data_frame(trajectory_data,timed_vehicle_data)
        except Exception as e:
            self.logger.error(f"Failed to extract data: {e}")