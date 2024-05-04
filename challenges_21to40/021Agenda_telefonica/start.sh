#!/bin/bash

# Iniciar o PostgreSQL
service postgresql start

# Exporta as variáveis de ambiente para o PostgreSQL
export PGUSER=my_user
export PGPASSWORD=my_password
export PGDATABASE=my_database

# Criar um banco de dados
psql -U $PGUSER -d $PGDATABASE -c "CREATE DATABASE IF NOT EXISTS $PGDATABASE;"

# Iniciar sua aplicação Python
python main.py