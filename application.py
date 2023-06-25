from flask import Flask, request
import json

application = Flask(__name__)

@application.route('/')
def home():
    return 'Home Page'

@application.route('/hello', methods=['GET'])
def hello_world():
    name = request.args.get('name', 'Schatzi')
    return f'Hello {name}!'

@application.route('/test-json', methods=['POST'])
def handle_post():
    data = request.get_json()
    email = data['email']
    datetime = data['datetime']
    questionnaire = data['questionnaire']
    context = data['context']
    
    return json.dumps(f'Hello {email}, {datetime}, {questionnaire}, {context}!'), 200
