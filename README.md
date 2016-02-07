# Example Docker Setup

This is an example setup using:

- `docker 1.10.0`
- `docker-compose 1.6.0`
- `docker-machine 0.6.0`

Compose was used to setup 4 services: `postgres`, `redis`, `worker` and `web`.
They are connected with a common network named `backend`. The containers `worker` and `web` are
typical app services connected to storage services `postgres` and `redis`. The
storage services use a common volume named `data`.

## Endpoints

### GET `:8000/`

> Responds with `Hello, world`.

### POST `:8000/items`

> Enqueues a `record_item` job. Accepts a json object with string keys/values.

### GET `:8000/items`

> Retrieves recorded items

## Instructions

1. Create a docker machine

2. Use docker machine

  ```shell
  eval $(docker-machine env your-machine-name)
  ```

2. Create a .env file:

  ```shell
  POSTGRES_PASSWORD=password
  POSTGRES_DB=app
  REDIS_URL=redis://redis:6379/0
  ```

3. Build app image

  ```shell
  docker build --rm -t app .
  ```

4. Create containers

  ```shell
  docker-compose up -d
  ```

5. Setup postgres

  ```shell
  docker exec -ti dockersetup_postgres bash
  su postgres
  echo "create extension store" | psql app
  echo "create table items (item hstore)" | psql app
  ```

