# Bot de Telegram de Recomendación de Podcast

Este proyecto es un bot de Telegram desarrollado en Python utilizando la librería `pyTelegramBotAPI`. Su propósito es recomendar capítulos del podcast "Las auténticas señoras de la calle Lista" a los usuarios, responder a comandos específicos y proporcionar información sobre los capítulos más recientes.

## Descripción

Este bot de Telegram realiza las siguientes funciones:

- **Recomendar Capítulos**: Ofrece recomendaciones aleatorias de capítulos del podcast "Las auténticas señoras de la calle Lista".
- **Capítulo Más Reciente**: Muestra el capítulo más reciente del podcast.
- **Búsqueda de Capítulos**: Permite a los usuarios buscar capítulos por palabras clave en el título o descripción.

## Cómo Usar el Bot

El bot está disponible en Telegram como [@CharoCalleListaBot](https://t.me/CharoCalleListaBot). A continuación, se describen los comandos y cómo interactuar con el bot:

1. **Iniciar el Bot**:
   - Envía el comando `/start` para iniciar el bot. El bot te enviará un mensaje de bienvenida con opciones para interactuar.

2. **Recomendar un Capítulo**:
   - Utiliza el botón "Recomendar un episodio" en el mensaje de bienvenida para recibir una recomendación aleatoria de un capítulo del podcast.

3. **Capítulo Más Reciente**:
   - Utiliza el botón "Episodio más reciente" en el mensaje de bienvenida para obtener información sobre el capítulo más reciente del podcast.

4. **Buscar un Capítulo**:
   - Envía el comando `/buscar` seguido de una palabra clave para buscar capítulos que coincidan con esa palabra clave en el título o descripción. Por ejemplo: `/buscar tecnología`.

## Configuración

Sigue estos pasos para configurar y ejecutar el bot en tu entorno local:

1. **Clonar el Repositorio**: Clona este repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/tu_usuario/Bot-de-Telegram.git
    ```

2. **Instalar Dependencias**: Navega al directorio del proyecto y utiliza `pip` para instalar las dependencias necesarias:

    ```bash
    cd Bot-de-Telegram
    pip install -r requirements.txt
    ```

3. **Obtener Token de Bot**: Crea un nuevo bot en Telegram utilizando el BotFather y obtén el token del bot recién creado.

4. **Configurar el Token**:
    - Crea un archivo `.env` en el directorio raíz del proyecto.
    - Abre el archivo `.env` en un editor de texto y agrega la siguiente línea, reemplazando `"TU_TOKEN_AQUÍ"` con el token obtenido en el paso anterior:

    ```plaintext
    TELEGRAM_TOKEN=TU_TOKEN_AQUÍ
    ```

5. **Asegurarse de que `.env` esté en `.gitignore`**:
    - Asegúrate de que el archivo `.env` esté incluido en `.gitignore` para que no se suba al repositorio. El contenido de `.gitignore` debería incluir `.env`:

    ```plaintext
    .env
    ```

6. **Ejecutar el Bot**: Ejecuta el script `main.py` utilizando Python para iniciar el bot:

    ```bash
    python main.py
    ```

## Funcionalidades

El bot actualmente cuenta con las siguientes funcionalidades:

- **Comando `/start`**: Inicia el bot y muestra un mensaje de bienvenida al usuario con opciones para recomendar un capítulo o ver el capítulo más reciente.
  
- **Comando `/buscar`**: Permite a los usuarios buscar capítulos por palabras clave.

- **Recomendación Aleatoria**: Ofrece un capítulo aleatorio del podcast "Las auténticas señoras de la calle Lista" como recomendación.

- **Capítulo Más Reciente**: Proporciona información sobre el capítulo más reciente del podcast.


## Personalización

Para agregar nuevas funcionalidades o personalizar el comportamiento del bot, puedes modificar el archivo `main.py` según tus necesidades. La documentación de `pyTelegramBotAPI` puede ser útil para comprender cómo extender la funcionalidad del bot.

## Autoría

Este proyecto fue desarrollado por [Eduardo Hernández Guzmán](https://github.com/EduardoHernandezGuzman). Puedes encontrar más proyectos interesantes en mi perfil de GitHub.
