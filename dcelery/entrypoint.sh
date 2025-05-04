#!/bin/bash

echo "Executando migrações do Django..."
python manage.py migrate

echo "Iniciando o servidor Django..."
exec "$@"
