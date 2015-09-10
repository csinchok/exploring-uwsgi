import os


def list_stats():
    yield b'<html><head><title>uwsgi metrics</title></head><body>'
    yield b'<table><tr><th>metric</th><th>value</th></tr>'
    for filename in os.listdir('metrics'):

        metric = 'N/A'

        with open(os.path.join('metrics', filename), 'r') as f:
            metric = f.read()

        if len(metric) == 1:
            metric = 'N/A'

        line = '<tr><td>{filename}</td><td>{metric}</td></tr>'.format(
            filename=filename,
            metric=metric
        )
        yield line.encode('utf-8')

    yield b'</table></body></html>'


def stats(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    return list_stats()
