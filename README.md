![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Documentation](https://img.shields.io/badge/doc-generated%20by%20dbt%20docs-yellow)](https://data-engineering-dwh.netlify.app/#!/overview)
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

# Deployment

> To deploy this project <br>`docker and docker-compose are required`

```bash
  git clone https://github.com/Nathnael12/DataEngineering_Datawarehouse_airflow.git
  cd DataEngineering_Datawarehouse_airflow
  pip install -r requirements.txt
  cd airflow
  docker-compose build
  docker-compose up -d

#   after this you can find airflow webserver at localhost:8080
#  you can either manually trig tasks or you can turn dags on to start scheduled tasks
```
## Redash Setup

First cd to redash directory 
```
cd redash
```
## Create an environment file here
`.env` Shoud contain the following
```bash
REDASH_HOST=http://localhost/redash
PYTHONUNBUFFERED=0
REDASH_LOG_LEVEL=INFO
REDASH_REDIS_URL=redis://redis:6379/0
POSTGRES_PASSWORD=password
REDASH_COOKIE_SECRET=redash-selfhosted
REDASH_SECRET_KEY=redash-selfhosted
REDASH_DATABASE_URL={postgresql+psycopg2://username:password@host/dbname}
```
Then run 

```bash
docker-compose run --rm server create_db 
docker-compose up -d

# your redash dashboard should be running on port 5000
```

Please, find the deployed dbt warehouse documentation from [here](https://data-engineering-dwh.netlify.app/#!/overview)


# Screenshots
### Airflow & DBT
Two Dags
![App Screenshot](./screenshots/DAGs.jpg)

Acyclic Graph representation
![App Screenshot](./screenshots/Directed%20Asyclic%20Graph.jpg)

Dbt tasks with graph
![App Screenshot](./screenshots/dbt-dags.jpg)

DBT docs
![App Screenshot](./screenshots/docs.jpg)

## redash Dashboard
![App Screenshot](./screenshots/redash-board%20I.jpg)

![App Screenshot](./screenshots/redash-board%20II.jpg)

<br>

# Tech Stacks


<img height="80" src="https://user-images.githubusercontent.com/25181517/117208740-bfb78400-adf5-11eb-97bb-09072b6bedfc.png">
<img height="80" src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png">
<img height="80" src="https://static-00.iconduck.com/assets.00/airflow-icon-512x512-tpr318yf.png">
<img height="80" src="https://seeklogo.com/images/D/dbt-logo-500AB0BAA7-seeklogo.com.png">
<img height="80" src="https://avatars.githubusercontent.com/u/10746780?s=280&v=4">

<br>

- postgreSql
- Docker
- Airflow
- DBT
- Docker


# Authors

- [@Nathnael12](https://www.github.com/nathnael12)


# Contributing

Contributions are always welcome!


Please adhere to this project's `code of conduct`.


## Feedback

If you have any feedback, please reach out to me at natnaelmasresha@gmail.com


