# Get started

## PostgreSQL

```bash
sudo su - postgres
psql
CREATE DATABASE truteordare;
CREATE USER truteordare WITH PASSWORD 'truteordare';
ALTER ROLE truteordare SET client_encoding TO 'utf8';
ALTER ROLE truteordare SET default_transaction_isolation TO 'read committed';
ALTER ROLE truteordare SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE truteordare TO truteordare;
```

## Read environment variables

```bash
set -o allexport; source ~/code/website/.env; set +o allexport
```
