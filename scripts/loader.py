import pandas as pd
from logger import Logger
class DataLoader():
    
    def __init__(self):
        self.logger=Logger().get_app_logger()
        self.logger.info('Data loader object Initialized')
    
    def get_columns_and_rows(file_path)->tuple:
        with open('../data/20181024_d1_0830_0900.csv','r') as f:
            lines=f.readlines()

        columns=lines[0].replace('\n','').split(';')
        data=lines[1:]
        return columns,data

