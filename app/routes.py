from app import app

@app.route('/')
def index1():
    html = '<h1> Index 1 </h1>'
    html += '<p> This is the response for the slash route </p>'
    return html

@app.route('/index')
def index2():
    html = '<h1> Index 1 </h1>'
    html += '<p> This is the response for the slash route index </p>'
    return html

