gunicorn -w 4 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src django_02.wsgi --timeout 60 --log-level debug --max-requests 10000
