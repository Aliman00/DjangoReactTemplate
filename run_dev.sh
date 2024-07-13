#!/bin/bash
trap "exit" INT TERM ERR
trap "kill 0" EXIT

python manage.py runserver &
cd frontend && npm start