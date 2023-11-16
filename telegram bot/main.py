import telebot
from pyowm import OWM
from config import OPENWEATHER_API_KEY, TELEGRAM_BOT_TOKEN

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
owm = OWM(OPENWEATHER_API_KEY)

def send_startup_message(bot_token, channel_id):
    bot = telebot.TeleBot(bot_token)
    message = "Бот запущен"
    bot.send_message(channel_id, message)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Отправьте город, в котором хотите узнать погоду.")

@bot.message_handler(func=lambda message: True)
def send_weather(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    status = w.detailed_status
    text = f"Текущая погода в {message.text}:\n{status}, {temp}°C"
    bot.reply_to(message, text)

bot.polling()