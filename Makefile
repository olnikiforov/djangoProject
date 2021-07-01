include .env
MANAGE = python3 manage.py
PROJECT_DIR = $(shell pwd)
WSGI_PORT=8000
RUN_COMMAND=gunicorn-run


run:
	$(MANAGE) runserver 0.0.0.0:$(WSGI_PORT)

make-migration:
	$(MANAGE)  makemigrations

migrate:
	$(MANAGE) migrate

lint:
	flake8 .


gunicorn_run_8081:
	gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR) django_02.wsgi --timeout 60 --log-level debug --max-requests 100004

collect_static:
	$(MANAGE) collectstatic

run_nginx:
	systemctl start nginx

stop_nginx:
	systemctl stop nginx

reload_nginx:
	systemctl reload nginx

celery-run:
	celery -A djangoProject worker -l INFO

celerybeat-run:
	rm -rf celerybeat.pid && celery -A djangoProject beat -l INFO


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


dkr-up-dev: dkr-down
	$(eval RUN_COMMAND=run)
	docker-compose up -d --build
	make copy-static

dkr-up-prod: dkr-down
	$(eval RUN_COMMAND=gunicorn-run)
	docker-compose up -d --build
	make docker collect-static
	make copy-static

dkr-down:
	docker-compose down

dkr-nmigrations:
	docker exec -it ssb-backend $(MANAGE) makemigrations

dkr-migrate:
	docker exec -it ssb-backend $(MANAGE) migrate --noinput

dkr-runserver:
	docker exec -it ssb-backend $(MANAGE) runserver 0.0.0.0.:9000

dkr-ini-env:
	cp .env.example env.my

copy-static:
	docker exec -it ssb-backend python ./src/manage.py collectstatic --noinput
	docker cp ssb-backend:/tmp/static_content/static /tmp/static
	docker cp /tmp/static nginx:/etc/nginx;

dkr-runserver-breakpoint:
	docker exec -it ssb-backend $(MANAGE) runserver 0.0.0.0:9000