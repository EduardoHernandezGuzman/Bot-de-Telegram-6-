import os
import random
import telebot
import feedparser
from flask import Flask
from dotenv import load_dotenv
from telebot import types
import threading

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

RSS_FEED_URL = 'https://anchor.fm/s/f174e400/podcast/rss'
feed = feedparser.parse(RSS_FEED_URL)
IMAGE_URL = 'https://s3-us-west-2.amazonaws.com/anchor-generated-image-bank/production/podcast_uploaded_nologo400/40409696/40409696-1715024081563-bc52ea9df01e4.jpg'

app = Flask(__name__)

@app.route('/')
def home():
    return "El bot de Telegram está funcionando!"

@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.InlineKeyboardMarkup()
    btn_recomendar = types.InlineKeyboardButton('Recomendar un episodio', callback_data='recomendar')
    btn_reciente = types.InlineKeyboardButton('Episodio más reciente', callback_data='reciente')
    markup.add(btn_recomendar, btn_reciente)

    start_text = """
    ¡Hola! Soy Charito, tu bot de recomendación de podcasts.
    ...
    Usa los botones a continuación para interactuar conmigo o escribe /buscar seguido de la palabra clave para buscar un episodio.
    """
    
    bot.send_photo(message.chat.id, IMAGE_URL)
    bot.send_message(message.chat.id, start_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'recomendar':
        recomendar_episodio(call.message)
    elif call.data == 'reciente':
        episodio_reciente(call.message)

@bot.message_handler(commands=['buscar'])
def buscar_episodio(message):
    try:
        query = message.text.split(' ', 1)[1].lower()
    except IndexError:
        bot.reply_to(message, "Por favor, proporciona una palabra clave después del comando /buscar.")
        return
    
    resultados = [e for e in feed.entries if query in e.title.lower() or query in e.description.lower()]
    
    if resultados:
        respuesta = "Aquí tienes algunos episodios que coinciden con tu búsqueda:\n\n"
        for episodio in resultados[:5]:
            respuesta += f"{episodio.title}\n{episodio.link}\n\n"
        bot.reply_to(message, respuesta)
    else:
        bot.reply_to(message, "No encontré ningún episodio que coincida con tu búsqueda.")

def recomendar_episodio(message):
    episodio = random.choice(feed.entries)
    titulo = episodio.title
    enlace = episodio.link
    bot.send_message(message.chat.id, f"Te recomiendo este episodio: {titulo}\n{enlace}")

def episodio_reciente(message):
    episodio = feed.entries[0]
    titulo = episodio.title
    enlace = episodio.link
    bot.send_message(message.chat.id, f"El episodio más reciente es: {titulo}\n{enlace}")

def start_bot():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)