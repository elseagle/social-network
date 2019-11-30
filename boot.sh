#!/bin/sh
source venv/bin/activate
flask deploy
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - flasky:app