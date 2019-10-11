
from flask import Flask, render_template, request
from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('Nshweta')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == "__main__":
    app.run()
