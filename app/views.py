# from http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Valid"
