#!/bin/bash
cd /app

./initialize.sh
exec ./manage.py runserver --noreload 0.0.0.0:8000
