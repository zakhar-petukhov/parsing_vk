#!/usr/bin/env bash

echo "Create virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "Install requirements"
cd .. && pip install -r requirements.txt

echo "Initialization database"
cd application
alembic upgrade head
alembic revision --autogenerate -m "create tables"


echo "Build Docker and start docker-compose"
cd ..
docker-compose up -d
