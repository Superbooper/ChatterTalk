from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
logging.basicConfig(level = logging.INFO)

chatbot = ChatBot(
    'A i',
    storage_adapter = 'chatterbot.storage.SQLStorageAdapter',
    logic_adapters = [
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
    ],
    database_uri = 'sqlite:///database.sqlite3',
)

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)

def converse(user_input):
    '''
    sends given input to chatterbot and gives back response
    gets user input: string
    reurns response: string
    '''
    response = chatbot.get_response(user_input)
    return response
