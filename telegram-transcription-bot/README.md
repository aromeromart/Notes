# 🎤 Bot de Telegram para Transcripción de Audio

Bot de Telegram que transcribe mensajes de voz y archivos de audio a texto usando OpenAI Whisper.

## ✨ Características

- 🎵 Transcribe mensajes de voz de Telegram
- 📁 Soporta archivos de audio (MP3, WAV, OGG, M4A, WebM)
- 🧠 Usa OpenAI Whisper para transcripción de alta calidad
- 🌍 Optimizado para español (configurable)
- 🔒 Procesamiento seguro (archivos se eliminan después del procesamiento)
- ⚡ Interfaz intuitiva con emojis y comandos

## 🚀 Instalación

### Prerrequisitos

1. **Python 3.8+** instalado
2. **Token de Bot de Telegram** (obtenerlo de @BotFather)
3. **API Key de OpenAI** (crear cuenta en OpenAI)
4. **FFmpeg** instalado (para procesamiento de audio)

### Pasos de instalación

1. **Clonar o descargar el proyecto:**
```bash
git clone <tu-repositorio>
cd telegram-transcription-bot
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno:**
```bash
# Copiar el archivo de ejemplo
cp .env.example .env

# Editar el archivo .env con tus credenciales
nano .env
```

4. **Configurar el archivo .env:**
```env
# Token del bot de Telegram (obténlo de @BotFather)
TELEGRAM_BOT_TOKEN=1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ

# API Key de OpenAI
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Configuración opcional
MAX_FILE_SIZE_MB=25
ALLOWED_AUDIO_FORMATS=mp3,wav,ogg,m4a,webm
```

## 📝 Configuración del Bot de Telegram

1. **Crear el bot:**
   - Habla con [@BotFather](https://t.me/botfather) en Telegram
   - Envía `/newbot`
   - Sigue las instrucciones y elige un nombre y username
   - Guarda el token que te proporcione

2. **Configurar el bot (opcional):**
   - Envía `/setdescription` para agregar una descripción
   - Envía `/setcommands` y pega:
     ```
     start - Iniciar el bot
     help - Mostrar ayuda
     info - Información del bot
     ```

## 🎯 Uso

### Ejecutar el bot

```bash
python bot.py
```

El bot se iniciará y estará listo para recibir mensajes.

### Comandos disponibles

- `/start` - Mensaje de bienvenida
- `/help` - Ayuda sobre cómo usar el bot
- `/info` - Información técnica del bot

### Cómo usar

1. **Busca tu bot** en Telegram usando el username que configuraste
2. **Envía `/start`** para activar el bot
3. **Envía un mensaje de voz** o **archivo de audio**
4. **Espera unos segundos** mientras se procesa
5. **Recibe la transcripción** en texto

## 🔧 Configuración Avanzada

### Cambiar idioma de transcripción

En el archivo `bot.py`, línea 141, puedes cambiar:
- `language="es"` para español
- `language="en"` para inglés
- Quitar el parámetro para detección automática

### Ajustar límites

En el archivo `.env`:
- `MAX_FILE_SIZE_MB` - Tamaño máximo de archivo en MB
- `ALLOWED_AUDIO_FORMATS` - Formatos permitidos separados por comas

## 📊 Límites y Restricciones

- **Tamaño máximo:** 25MB por archivo
- **Duración recomendada:** Hasta 10 minutos
- **Formatos soportados:** MP3, WAV, OGG, M4A, WebM
- **Idiomas:** Optimizado para español, soporta múltiples idiomas

## 🚀 Despliegue en Producción

### Opciones de hosting

1. **Heroku** (gratuito con limitaciones)
2. **Railway** (fácil despliegue)
3. **VPS** (mayor control)
4. **Google Cloud Run** (pago por uso)

### Ejemplo para Heroku

1. Crear `Procfile`:
```
worker: python bot.py
```

2. Configurar variables de entorno en Heroku
3. Desplegar usando Git

## 🛠️ Desarrollo

### Estructura del proyecto

```
telegram-transcription-bot/
├── bot.py              # Código principal del bot
├── requirements.txt    # Dependencias de Python
├── .env.example       # Ejemplo de configuración
├── .env              # Tu configuración (no subir a Git)
└── README.md         # Este archivo
```

### Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a tu rama
5. Crea un Pull Request

## 🐛 Solución de Problemas

### Error: "TELEGRAM_BOT_TOKEN no está configurado"
- Verifica que el archivo `.env` existe
- Asegúrate de que el token esté correctamente configurado

### Error: "OPENAI_API_KEY no está configurado"
- Verifica tu API Key de OpenAI
- Asegúrate de tener créditos en tu cuenta de OpenAI

### Error: "No pude transcribir el audio"
- Verifica la calidad del audio
- Asegúrate de que el audio tenga voz humana
- Intenta con un archivo más pequeño

### FFmpeg no encontrado
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Descargar desde https://ffmpeg.org/download.html
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.

## 🤝 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de solución de problemas
2. Crea un issue en el repositorio
3. Contacta al desarrollador

---

**¡Disfruta transcribiendo tus audios! 🎉**

XX tenemos un código de chatbot que al final hay que alojarlo,
xx jon el youtuber habla de hostsginger como el mejor punto de alojamiento
xx usar metano-ia.org para comunicarme con León 
