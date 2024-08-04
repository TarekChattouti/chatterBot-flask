from chatterbot import ChatBot



chatbot = ChatBot(
    'ExampleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response


if __name__ == "__main__":
    print("Hello! I'm a chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = get_response(user_input)
        if response.confidence >= 0.9:
            print(f"Bot: {response}")
        else:
            print("I am not confident enough to respond to that.")
        
        
