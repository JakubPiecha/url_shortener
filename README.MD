
[![Sphinx](https://img.shields.io/badge/documentation-yes-green
)](https://choosealicense.com/licenses/mit/)
![pytest-cov](https://img.shields.io/badge/coverage-100%25-green?color=green)
[![Beerware license](https://img.shields.io/badge/license-Beerware-yellow
)](https://github.com/JakubPiecha/url_shortener/blob/master/LICENSE)



# URL Shortener

Django Rest Framework-based URL Shortener app. This robust and secure platform allows you to effortlessly shorten long URLs, making them more user-friendly and easy to share. With RESTful APIs, you can seamlessly integrate URL shortening into your applications and services.


## Demo

[URL Shortener heroku](https://salty-eyrie-21851-de0797a7d781.herokuapp.com/api/schema/swagger-ui/)


## Tech Stack

**Server:** Python, Django, Django Rest Framework, Docker, Postgres, Redis


## Run Locally

Clone the project

```bash
  git clone https://github.com/JakubPiecha/url_shortener.git
```

Go to the project directory

```bash
  cd url_shortener
```

Set Environment Variables

```bash
  cp ./envs/api.default.env ./envs/api.env  
  cp ./envs/postgres.default.env ./envs/postgres.env 
  cp ./envs/redis.default.env ./envs/redis.env 
  # set variable values
```

Start docker containers
```bash
  docker compose up
```


Go to your client and types
```bash
 http://0.0.0.0:8000/api/schema/swagger-ui/ 
 or
 http://localhost:8000/api/schema/swagger-ui/ 
```
You can use Postman with predefined Postman collections:
- load postman collections from ./api/postman_collections/*.postman_collection.json

## Set Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

`DJ_SECRET_KEY=` - django secret key for CSRF [gist](https://gist.github.com/JakubPiecha/0ccae2a55b9413c484a5d991ce0540ed)

`DJ_DEBUG=` - production development mode

`DJ_ALLOWED_HOSTS=` - Allowed hosts for Django

`DJ_CSRF_TRUSTED_ORIGINS=` - Domain list for validation

`LOGGING_LVL=` Python logging package levels

`DJ_SU_USERNAME=` - Default superuser name

`DJ_SU_PASSWORD=` - Default superuser email

`DJ_SU_EMAIL=` - Default superuser password


Also variables to your ./envs/postgres.env file

`POSTGRES_USER=` - Postgres root user

`POSTGRES_PASSWORD=` - Postgres root password

`POSTGRES_DB=` - Database name

`POSTGRES_HOST=` Database host need to add docker service name

`POSTGRES_PORT=` Database ports

Variables for Redis ./envs/redis.env file

`REDIS_HOST=` - Running server Redis host

`REDIS_PORT=` - Running server Redis port


## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/JakubPiecha/url_shortener/master/screenshots/test_coverage.png)


## Author

- [@JakubPiecha](https://github.com/JakubPiecha)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/JakubPiecha?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jakubpiecha/)


