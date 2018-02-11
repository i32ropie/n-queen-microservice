import telebot
import requests

token = "" # Bot token given via https://t.me/botfather

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_handler(m):
    cid = m.chat.id
    welcome = "Welcome to this bot. The objetive of this bot is to show how the microservice works. The available commands are:\n{}".format('\n'.join(['/{}'.format(x) for x in range(4, 11)]))
    bot.send_message(cid, welcome)

@bot.message_handler(commands=[str(x) for x in range(4,11)])
def n_queen(m):
    cid = m.chat.id
    number = m.text.strip('/')
    url = 'http://0.0.0.0:8000/get_n_queen_solutions'
    params = {'n': number}
    r = requests.get(url, params)
    r = r.json()['success']
    for x in r:
        bot.send_message(cid, '`{}`'.format(x), parse_mode="Markdown")

bot.polling(True)
