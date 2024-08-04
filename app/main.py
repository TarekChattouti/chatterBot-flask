from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify
import os
import nltk

# Set a custom NLTK data directory
nltk_data_path = '/app/custom_nltk_data'
os.makedirs(nltk_data_path, exist_ok=True)
nltk.data.path.append(nltk_data_path)

# Download necessary NLTK data
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.download('wordnet', download_dir=nltk_data_path)

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

        
