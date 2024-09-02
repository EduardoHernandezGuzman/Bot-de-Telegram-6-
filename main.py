import telebot
import feedparser
from dotenv import load_dotenv
import os
import random

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

RSS_FEED_URL = 'https://anchor.fm/s/f174e400/podcast/rss'

feed = feedparser.parse(RSS_FEED_URL)

# Comando /start
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Soy tu bot de recomendación de podcasts.
    
    Usa los siguientes comandos:
    
    /recomendar - Recomienda un episodio aleatorio
    /reciente - Muestra el episodio más reciente
    /buscar - Buscar un episodio por palabra clave
    """
    bot.reply_to(message, start_text)

# Comando /recomendar
@bot.message_handler(commands=['recomendar'])
def recomendar_episodio(message):
    episodio = random.choice(feed.entries)
    titulo = episodio.title
    enlace = episodio.link
    bot.reply_to(message, f"Te recomiendo este episodio: {titulo}\n{enlace}")

# Comando /reciente
@bot.message_handler(commands=['reciente'])
def episodio_reciente(message):
    episodio = feed.entries[0]
    titulo = episodio.title
    enlace = episodio.link
    bot.reply_to(message, f"El episodio más reciente es: {titulo}\n{enlace}")

# Comando /buscar
@bot.message_handler(commands=['buscar'])
def buscar_episodio(message):
    query = message.text.split(' ', 1)[1].lower()  
    resultados = [e for e in feed.entries if query in e.title.lower() or query in e.description.lower()]
    
    if resultados:
        respuesta = "Aquí tienes algunos episodios que coinciden con tu búsqueda:\n\n"
        for episodio in resultados[:5]:  
            respuesta += f"{episodio.title}\n{episodio.link}\n\n"
        bot.reply_to(message, respuesta)
    else:
        bot.reply_to(message, "No encontré ningún episodio que coincida con tu búsqueda.")

if __name__ == "__main__":
    bot.polling(none_stop=True)