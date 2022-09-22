
def model(dbt, session):
  
    my_sql_model_df = dbt.ref("ten_vehicles")
    
    final_df = my_sql_model_df.head()
    
    return final_df