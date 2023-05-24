from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    custom_greeting = os.environ.get('CUSTOM_GREETING', 'Hello, World!')
    return custom_greeting

@app.route('/data')
def data():
    return '3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
