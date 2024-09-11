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

* Ejecutar:

`fastapi dev sqlalchemy-dividido/api.py`
