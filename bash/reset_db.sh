#!/bin/bash
sudo rm -rf ./app/*/migrations/

sudo docker exec -it pwf-db psql -U pwfood postgres -c  "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid <> pg_backend_pid() AND datname = 'pwfood';"
sudo docker exec -it pwf-db psql -U pwfood postgres -c  "DROP DATABASE pwfood;"
sudo docker exec -it pwf-db psql -U pwfood postgres -c  "CREATE DATABASE pwfood;"


sudo docker exec pwf-admin python manage.py makemigrations blog
sudo docker exec pwf-admin python manage.py makemigrations categories
sudo docker exec pwf-admin python manage.py makemigrations recipes

sudo docker exec pwf-admin python manage.py makemigrations
sudo docker exec pwf-admin python manage.py migrate
