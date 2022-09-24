# please create an environment file here
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
____
Then run 

```bash
docker-compose run --rm server create_db 
docker-compose up -d
# your redash should be running on port 5000
```