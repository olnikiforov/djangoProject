include .env
MANAGE = python3 manage.py
PROJECT_DIR = $(shell pwd)
WSGI_PORT=8000
RUN_COMMAND=gunicorn-run


run:
	$(MANAGE) runserver 0.0.0.0:$(WSGI_PORT)

make-migration:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE)manage.py migrate

lint:
	flake8 .

gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:8081 --chdir $(shell pwd) djangoProject.wsgi --timeout 60 --log-level debug --max-requests 10000

celery-run:
	celery -A djangoProject worker -l INFO

celerybeat-run:
	rm -rf celerybeat.pid && celery -A djangoProject beat -l INFO

collect_static:
	$(MANAGE)collectstatic

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
