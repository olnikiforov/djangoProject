run:
	python manage.py runserver

make-migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

lint:
	flake8 .
gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir /home/shs/Documents/prog/djangoProject/ djangoProject.wsgi --timeout 60 --log-level debug --max-requests 10000

collect_static:
	python manage.py collectstatic

run_nginx:
	systemctl start nginx

stop_nginx:
	systemctl stop nginx

reload_nginx:
	systemctl reload nginx
