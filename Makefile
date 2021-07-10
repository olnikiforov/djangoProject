run:
	python manage.py runserver 0.0.0.0:8000

make-migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

lint:
	flake8 .
gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir $(shell pwd) djangoProject.wsgi --timeout 60 --log-level debug --max-requests 10000

collect_static:
	python manage.py collectstatic

run_nginx:
	systemctl start nginx

stop_nginx:
	systemctl stop nginx

reload_nginx:
	systemctl reload nginx


test:
	pytest

test_run:
	pytest --cov=main --cov-report=html --cov-fail-under=40
	xdg-open static_content/coverage/index.html

dkr-run:
	docker run --rm -t -d -p 8001:8111 --name ssb ssb:1.0

dkr-bld:
	docker build -t ssb:1.0 .

dkr-st:
	docker container stop ssb

urls:
	python3 manage.py show_urls