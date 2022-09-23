![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Data Engineering: Data warehouse tech stack with Postgres, DBT, and Airflow

You and your colleagues have joined to create an AI startup that deploys sensors to businesses, collects data from all activities in a business - people’s interaction, traffic flows, smart appliances installed in a company. Your startup helps organizations obtain critical intelligence based on public and private data they collect and organize. 

A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. Your startup is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras.

The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.  Unlike the Extract, Transform, Load (ETL), the ELT framework helps analytic engineers in the city traffic department setup transformation workflows on a need basis.  

___

This project tried to implement the following core tasks
- A “data warehouse” (PostgresQL)
- An orchestration service (Airflow)
- An ELT tool (dbt)
___

## Deployment

> To deploy this project <br>`docker and docker-compose are required`

```bash
  git clone https://github.com/Nathnael12/DataEngineering_Datawarehouse_airflow.git
  cd DataEngineering_Datawarehouse_airflow
  pip install -r requirements.txt
  cd airflow
  docker-compose up airflow-init
  docker-compose up

#   after this you can find airflow webserver at localhost:8080
#  you can either manually trig tasks or you can turn dags on to start scheduled tasks
```
Please, find the deployed dbt warehouse documentation from [here](https://data-engineering-dwh.netlify.app/#!/overview)


## Screenshots
Two Dags
![App Screenshot](./screenshots/DAGs.jpg)

Acyclic Graph representation
![App Screenshot](./screenshots/Directed%20Asyclic%20Graph.jpg)

DBT docs
![App Screenshot](./screenshots/docs.jpg)

Simple lineage
![App Screenshot](./screenshots/simple%20linage.jpg)


## Tech Stack

- Airflow
- Postgres
- DBT
- Docker


## Authors

- [@Nathnael12](https://www.github.com/nathnael12)


## Contributing

Contributions are always welcome!


Please adhere to this project's `code of conduct`.


## Feedback

If you have any feedback, please reach out to me at natnaelmasresha@gmail.com


