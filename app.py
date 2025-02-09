from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Python Training!"

@app.route('/toys')
def toys():
    return "My toys"

@app.route('/cities')
def cities():
    return "My cities"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
