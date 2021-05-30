# djangoProject

Notices about this djangoProject
## Running gunicorn with collect_static

Use this to run gunicorn

```bash
make gunicorn_run_8081:
```

Running ngix
```bash
make run_nginx:
```

Stop ngix
```bash
make stop_nginx:
```

Reload ngix
```bash
make reload_nginx:
```

Use this to create static_content directory
```bash
make collect_static
```

## Nginx configuration

```
events {}
http {
	include /etc/nginx/mime.types;
	sendfile on;
	server {
		listen 80;
		listen [::]:80;
		server_name 127.0.0.1 blog.com;
		location /static/ {
			root /home/shs/Documents/prog/djangoProject/static_content;
		}
		location / {
			proxy_pass http://127.0.0.1:8081;
		}
	}
}
```


