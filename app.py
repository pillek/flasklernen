from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/wow')
def wow():
    return 'Wow, this is my second working URL!'