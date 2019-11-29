## Deploying to Heroku

- heroku git:remote -a <app_name>
- git push heroku master


## SQL

### Heroku Postgres
- https://www.heroku.com/postgres

- psycopg2

- DATABASE_URL = os.environ['DATABASE_URL']



## mongoDB

### mongoDB Atlas
- https://cloud.mongodb.com

- pymongo

- mongodb+srv://<user_name>:<password>@<database>.mongodb.net/test?retryWrites=true&w=majority