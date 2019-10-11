from chatterbot import ChatBot
chatbot = ChatBot('Nshweta')

while True:
        request = input('you: ')
        response = chatbot.get_response(request)
        print('Bot: ', response)
