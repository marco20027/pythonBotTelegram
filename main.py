import telebot
import json
from tabulate import tabulate
from texttable import Texttable
API_TOKEN = '6154235977:AAFt5Tt39HgUgko6rJTkPNMEUsvCcPxMMyI'

bot = telebot.TeleBot(API_TOKEN)

classifica = open("classifica.json")
data = json.load(classifica)
dataObject = str(data)
print(dataObject)

stats = tabulate([["Napoli", 90],["Lazio",  74],["Inter",  72],["Milan", 70],["Atalanta",64],["Roma",63],["Juventus",62],["Fiorentina",56],["Bologna",54],["Torino",53],["Monza",52],["Udinese",46],["Sassuolo",45],["Empoli",43],["Salernitana",42],["Lecce",36],["Verona",31],["Spezia",31],["Cremonese",27],["Sampdoria",19]], headers=["Squadra", "Pts"],tablefmt='orgtbl')

table = Texttable()
table.add_rows([["Squadra","Pt"],["Napoli", 90],["Lazio",  74],["Inter",  72],["Milan", 70],["Atalanta",64],["Roma",63],["Juventus",62],["Fiorentina",56],["Bologna",54],["Torino",53],["Monza",52],["Udinese",46],["Sassuolo",45],["Empoli",43],["Salernitana",42],["Lecce",36],["Verona",31],["Spezia",31],["Cremonese",27],["Sampdoria",19]])
print(table.draw())
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Ciao Benvenuto !\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(commands =['hello','saluta'])
def echo_message(message):
    bot.reply_to(message,"ciao!")


@bot.message_handler(commands =['classifica','stats'])
def statsSerieA(link):
    bot.reply_to(link, stats)


@bot.message_handler(commands=['acmilan'])
def acmilan(text):
    bot.reply_to(text, "La squadra migliore interista di merda !")


bot.polling()