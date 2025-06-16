# Cómo crear un nuevo bot en Telegram

Para crear un nuevo bot en Telegram, sigue estos pasos:

## 1. Buscar BotFather
- Abre Telegram y busca **@BotFather**
- Es el bot oficial de Telegram para crear y gestionar bots

## 2. Iniciar conversación con BotFather
- Envía `/start` para comenzar
- Verás una lista de comandos disponibles

## 3. Crear el bot
- Envía `/newbot`
- BotFather te pedirá:
  1. **Nombre del bot**: El nombre público que verán los usuarios (ej: "Mi Bot Genial")
  2. **Username del bot**: Debe terminar en "bot" (ej: "MiBotGenialBot" o "mi_bot_genial_bot")

## 4. Obtener el token
- Una vez creado, BotFather te dará un **token de acceso**
- Guarda este token de forma segura, lo necesitarás para programar el bot
- Formato: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

## 5. Configurar el bot (opcional)
Puedes usar estos comandos con BotFather:
- `/setdescription` - Descripción del bot
- `/setabouttext` - Texto "Acerca de"
- `/setuserpic` - Foto de perfil
- `/setcommands` - Lista de comandos disponibles

## 6. Comenzar a programar
Una vez tengas el token, puedes usar APIs como:
- **Python**: `python-telegram-bot`
- **Node.js**: `telegraf` o `node-telegram-bot-api`
- **C#**: `Telegram.Bot`
- **PHP**: `longman/telegram-bot`

## Ejemplo básico en Python
```python
import telebot

# Token obtenido de BotFather
TOKEN = 'TU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu nuevo bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
```

## Recursos útiles
- [Documentación oficial de Telegram Bot API](https://core.telegram.org/bots/api)
- [Guía oficial de Telegram para bots](https://core.telegram.org/bots)

