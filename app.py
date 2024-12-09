from bottle import route, run, template

@route('/')
def index():
    return template('Hello World')

run(host='0.0.0.0', port=80)