from flask import Flask, request

application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Home Page'

@application.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'Schatzi')
    return f'Hello {name}!'
