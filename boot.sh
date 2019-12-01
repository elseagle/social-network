#!/bin/sh
source venv/bin/activate
flask deploy
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - flasky:app


-e DATABASE_URL=mysql+pymysql://flasky:password@dbserver/flasky \
-e MAIL_DEFAULT_FROM=dowolebolu@gmail.com -e \ flasky:latest