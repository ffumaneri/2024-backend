# 2024-backend

## instalacion

`pip install -r requirements.txt`

O instalar los 3 paquetes individualmente:

Postgres:

`pip install psycopg2-binary`

FastApi:

`pip install "fastapi[standard]"`

SQLAlchemy:

`pip install sqlalchemy`

## subproyectos

### Basico

[SQL Alchemy Basico](./sqlalchemy-basico)

* Ejecutar:

`fastapi dev sqlalchemy-basico/main.py`

### Dividido por capas

[SQL Alchemy Dividido](./sqlalchemy-dividido)

Consta de 4 archivos:

api.py: Donde se define la API. Se usa [FastAPI](https://fastapi.tiangolo.com/)
db.py: Se define la conexión a la base de datos. Usamos la base de datos [PostgreSQL](https://www.postgresql.org/) y el driver [pyppsycopg2](https://www.psycopg.org/) para conectar con PostgreSQL con Python.
model.py: El mapeo de python con tablas de la base de datos. Usamos [SQLAlchemy](https://www.sqlalchemy.org/)
repository.py: Donde se crean las consultas a la base de datos. Usamos [SQLAlchemy](https://www.sqlalchemy.org/)

* Ejecutar:

`fastapi dev sqlalchemy-dividido/api.py`
