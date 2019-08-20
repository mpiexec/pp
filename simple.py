from flask import Flask

app = Flask(__name__)


@app.route('/')
def simple():
    return 'Simple web-service!'

@app.route('/ping')
def pp():
    return 'p0ng'
