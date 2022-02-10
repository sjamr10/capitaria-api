# Capitaria API
REST API for Capitaria.

## DB schema
Here is the db schema:
[schema.png](schema.png)

## SQL answers
You can find the SQL answers here:
[sql.md](sql.md)

## Prerequisites
* [Docker](https://www.docker.com/get-started)

## Clone repo
```sh
git clone git@github.com:sjamr10/capitaria-api.git
```

## Run project
Go to project directory and run:
```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```
Visit http://localhost:3000/docs to check API docs

## Run tests
Start DB if not already running:
```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d capitaria-postgres
```
```sh
docker-compose -f docker-compose.yml -f docker-compose.dev.yml run capitaria-api pytest-watch -- --last-failed --new-first
```
