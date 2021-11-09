from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

bot = ChatBot('Pybot')
bot = ChatBot(
    'Pybot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
    )
    
conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Olá',
    'Qual o seu nome?',
    'Pybot',
    'Prazer em te conhecer',
    'Igualmente!',
    'Tudo bem?',
    'Muito bem e você?',
    'Ótimo',
    'Papo bom o nosso',
    'kkk',
    'adeus',
    'Volte sempre!',
])

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.portuguese')
while True:
  resposta = bot.get_response(input("Usuário: "))
  if float(resposta.confidence) > 0.5:]
  print("Pybot: ", resposta)
else:
      print("Desculpe, eu não entendi!")
