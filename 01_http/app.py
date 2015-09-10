
def hello(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<html><head><title>Hello world.</title></head><body>Hello world.</body></html>']
