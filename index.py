from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>hello {{name}}</b>!',name=name)

@route('/')
def index():
    return '<h1>WELCOME TO NEW WORLD</h1>'


run(host='localhost', port=8080,debug=True,reloader=True)
