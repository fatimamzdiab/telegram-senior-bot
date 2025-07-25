import telebot
import os

TOKEN = os.environ.get("8433991841:AAE-3WOAWb_7nObQfcmjQtSqmuHB2c8tihY")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['بدء'])
def start(message):
    bot.send_message(message.chat.id, "ياهلا! معك أم محجوب لتجنب الرسوب")

bot.polling()
