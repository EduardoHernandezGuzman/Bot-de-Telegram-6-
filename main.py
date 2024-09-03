import telebot
import feedparser
from dotenv import load_dotenv
import os
import random
from telebot import types

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

RSS_FEED_URL = 'https://anchor.fm/s/f174e400/podcast/rss'

feed = feedparser.parse(RSS_FEED_URL)

# Comando /start
@bot.message_handler(commands=['start'])
def send_start(message):
    markup = types.InlineKeyboardMarkup()
    btn_recomendar = types.InlineKeyboardButton('Recomendar un episodio', callback_data='recomendar')
    btn_reciente = types.InlineKeyboardButton('Episodio más reciente', callback_data='reciente')
    markup.add(btn_recomendar, btn_reciente)

    start_text = """
    ¡Hola! Soy tu bot de recomendación de podcasts.
    
    Usa los botones a continuación para interactuar conmigo o escribe /buscar seguido de la palabra clave para buscar un episodio.
    """
    bot.send_message(message.chat.id, start_text, reply_markup=markup)

# Manejar las interacciones con los botones inline
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'recomendar':
        recomendar_episodio(call.message)
    elif call.data == 'reciente':
        episodio_reciente(call.message)

# Comando /buscar
@bot.message_handler(commands=['buscar'])
def buscar_episodio(message):
    # Verificar que el comando /buscar está seguido de una palabra clave
    try:
        query = message.text.split(' ', 1)[1].lower()
    except IndexError:
        bot.reply_to(message, "Por favor, proporciona una palabra clave después del comando /buscar.")
        return
    
    resultados = [e for e in feed.entries if query in e.title.lower() or query in e.description.lower()]
    
    if resultados:
        respuesta = "Aquí tienes algunos episodios que coinciden con tu búsqueda:\n\n"
        for episodio in resultados[:5]:  # Mostrar hasta 5 resultados
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

if __name__ == "__main__":
    bot.polling(none_stop=True)