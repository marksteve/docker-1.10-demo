# Example Docker Setup

This is an example setup using:

- `docker 1.10.0`
- `docker-compose 1.6.0`
- `docker-machine 0.6.0`

1. Create a docker machine

2. Use docker machine

  ```shell
  eval $(docker-machine env your-machine-name)
  ```

2. Create a .env file:

  ```
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

  ```
  docker exec -ti dockersetup_postgres bash
  su postgres
  echo "create extension store" | psql app
  echo "create table items (item hstore)" | psql app
  ```
