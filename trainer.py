from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json


chatbot = ChatBot(
    'ExampleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

with open('corpus.json', 'r') as f:
    data = json.load(f)


trainer = ListTrainer(chatbot)

for conversation in data['conversations']:
    trainer.train(conversation)