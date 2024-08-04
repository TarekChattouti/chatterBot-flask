from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify


chatbot = ChatBot(
    'ExampleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response


        
        

app = Flask(__name__)



@app.route('/api/get_response')
def index():
    user_input = request.args.get('msg')
    response = get_response(user_input)
    print(response)
    if response.confidence >= 0.9:
        return str(response)
    else:
        return "I dont understand..."

        
