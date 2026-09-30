release: python manage.py migrate --noinput
web: gunicorn core.wsgi --workers 3 --timeout 60 --access-logfile -
