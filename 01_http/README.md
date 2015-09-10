# HTTP

uWSGI can talk HTTP! This is very helpful. Try it out:

uwsgi --http=127.0.0.1:8080 --module=app:hello