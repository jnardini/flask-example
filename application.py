from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def home():
    return 'Home Page'

@application.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'Schatzi')
    return f'Hello {name}!'
