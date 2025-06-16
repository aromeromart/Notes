#!/usr/bin/env python3
"""
Bot de Telegram para transcripción de audio usando OpenAI Whisper
"""

import os
import logging
import tempfile
from pathlib import Path
from typing import Optional

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
from telegram.constants import ParseMode
from dotenv import load_dotenv
import openai
from pydub import AudioSegment

# Cargar variables de entorno
load_dotenv()

# Configuración de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Variables de configuración
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', '25'))
ALLOWED_FORMATS = os.getenv('ALLOWED_AUDIO_FORMATS', 'mp3,wav,ogg,m4a,webm').split(',')

# Configurar cliente de OpenAI
openai.api_key = OPENAI_API_KEY

class TranscriptionBot:
    def __init__(self):
        self.temp_dir = Path(tempfile.gettempdir()) / 'telegram_transcription_bot'
        self.temp_dir.mkdir(exist_ok=True)
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Comando /start"""
        welcome_message = """
🎤 *Bot de Transcripción de Audio*

¡Hola! Soy tu bot de transcripción de audio. 

Envíame cualquier mensaje de voz o archivo de audio y lo convertiré a texto usando OpenAI Whisper.

*Formatos soportados:* MP3, WAV, OGG, M4A, WebM
*Tamaño máximo:* 25MB

*Comandos disponibles:*
/start - Mostrar este mensaje
/help - Mostrar ayuda
/info - Información del bot

¡Envía tu audio y empezamos!
        """
        
        await update.message.reply_text(
            welcome_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Comando /help"""
        help_message = """
🎆 *Ayuda - Bot de Transcripción*

*Cómo usar el bot:*
1. Envía un mensaje de voz desde Telegram
2. O envía un archivo de audio
3. Espera unos segundos mientras proceso el audio
4. Recibe la transcripción en texto

*Consejos para mejores resultados:*
• Habla claramente y a velocidad normal
• Evita ruidos de fondo
• El audio debe estar en español o inglés
• Archivos más cortos se procesan más rápido

*Limitaciones:*
• Tamaño máximo: 25MB
• Duración recomendada: hasta 10 minutos
        """
        
        await update.message.reply_text(
            help_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Comando /info"""
        info_message = """
🤖 *Información del Bot*

*Tecnología:*
• OpenAI Whisper API para transcripción
• Python Telegram Bot
• Procesamiento de audio con PyDub

*Formatos soportados:*
• MP3, WAV, OGG, M4A, WebM
• Mensajes de voz de Telegram

*Privacidad:*
• Los archivos se procesan temporalmente
• Se eliminan después de la transcripción
• No se almacenan grabaciones
        """
        
        await update.message.reply_text(
            info_message,
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def transcribe_audio(self, audio_file_path: str, file_format: str) -> Optional[str]:
        """Transcribir audio usando OpenAI Whisper"""
        try:
            # Convertir a MP3 si es necesario
            mp3_path = audio_file_path
            if file_format.lower() != 'mp3':
                mp3_path = audio_file_path.replace(f'.{file_format}', '.mp3')
                audio = AudioSegment.from_file(audio_file_path, format=file_format)
                audio.export(mp3_path, format='mp3')
            
            # Transcribir con OpenAI Whisper
            with open(mp3_path, 'rb') as audio_file:
                transcript = openai.Audio.transcribe(
                    model="whisper-1",
                    file=audio_file,
                    language="es"  # Puedes cambiar a "en" para inglés o quitar para detección automática
                )
            
            return transcript.text
            
        except Exception as e:
            logger.error(f"Error en transcripción: {e}")
            return None
        finally:
            # Limpiar archivos temporales
            for file_path in [audio_file_path, mp3_path]:
                if os.path.exists(file_path):
                    os.remove(file_path)
    
    async def handle_voice_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Manejar mensajes de voz"""
        try:
            # Informar que se está procesando
            processing_message = await update.message.reply_text(
                "🎤 Procesando mensaje de voz...\n⏳ Esto puede tomar unos segundos."
            )
            
            # Obtener el archivo de voz
            voice_file = await context.bot.get_file(update.message.voice.file_id)
            
            # Verificar tamaño del archivo
            file_size_mb = voice_file.file_size / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                await processing_message.edit_text(
                    f"⚠️ El archivo es demasiado grande ({file_size_mb:.1f}MB).\n"
                    f"Tamaño máximo permitido: {MAX_FILE_SIZE_MB}MB"
                )
                return
            
            # Descargar archivo
            temp_file_path = self.temp_dir / f"voice_{update.message.message_id}.ogg"
            await voice_file.download_to_drive(temp_file_path)
            
            # Transcribir
            transcription = await self.transcribe_audio(str(temp_file_path), 'ogg')
            
            if transcription:
                # Enviar transcripción
                response_message = f"📝 *Transcripción:*\n\n{transcription}"
                await processing_message.edit_text(
                    response_message,
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await processing_message.edit_text(
                    "⚠️ No pude transcribir el audio. \n"
                    "Asegúrate de que el audio tenga buena calidad y esté en español."
                )
                
        except Exception as e:
            logger.error(f"Error procesando mensaje de voz: {e}")
            await update.message.reply_text(
                "⚠️ Ocurrió un error al procesar el mensaje de voz. \n"
                "Por favor, inténtalo de nuevo."
            )
    
    async def handle_audio_file(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Manejar archivos de audio"""
        try:
            # Informar que se está procesando
            processing_message = await update.message.reply_text(
                "🎵 Procesando archivo de audio...\n⏳ Esto puede tomar unos segundos."
            )
            
            # Obtener el archivo de audio
            audio_file = await context.bot.get_file(update.message.audio.file_id)
            
            # Verificar tamaño del archivo
            file_size_mb = audio_file.file_size / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                await processing_message.edit_text(
                    f"⚠️ El archivo es demasiado grande ({file_size_mb:.1f}MB).\n"
                    f"Tamaño máximo permitido: {MAX_FILE_SIZE_MB}MB"
                )
                return
            
            # Obtener extensión del archivo
            file_name = update.message.audio.file_name or "audio.mp3"
            file_extension = file_name.split('.')[-1].lower()
            
            # Verificar formato
            if file_extension not in ALLOWED_FORMATS:
                await processing_message.edit_text(
                    f"⚠️ Formato no soportado: {file_extension}\n"
                    f"Formatos permitidos: {', '.join(ALLOWED_FORMATS)}"
                )
                return
            
            # Descargar archivo
            temp_file_path = self.temp_dir / f"audio_{update.message.message_id}.{file_extension}"
            await audio_file.download_to_drive(temp_file_path)
            
            # Transcribir
            transcription = await self.transcribe_audio(str(temp_file_path), file_extension)
            
            if transcription:
                # Enviar transcripción
                response_message = f"📝 *Transcripción:*\n\n{transcription}"
                await processing_message.edit_text(
                    response_message,
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await processing_message.edit_text(
                    "⚠️ No pude transcribir el audio. \n"
                    "Asegúrate de que el audio tenga buena calidad y esté en español."
                )
                
        except Exception as e:
            logger.error(f"Error procesando archivo de audio: {e}")
            await update.message.reply_text(
                "⚠️ Ocurrió un error al procesar el archivo de audio. \n"
                "Por favor, inténtalo de nuevo."
            )
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Manejar documentos (archivos de audio enviados como documentos)"""
        try:
            document = update.message.document
            file_name = document.file_name or "unknown"
            file_extension = file_name.split('.')[-1].lower()
            
            # Verificar si es un archivo de audio
            if file_extension not in ALLOWED_FORMATS:
                await update.message.reply_text(
                    f"🤷‍♂️ Este tipo de archivo no es soportado para transcripción.\n"
                    f"Formatos de audio soportados: {', '.join(ALLOWED_FORMATS)}"
                )
                return
            
            # Procesar como archivo de audio
            processing_message = await update.message.reply_text(
                "🎵 Procesando archivo de audio...\n⏳ Esto puede tomar unos segundos."
            )
            
            # Verificar tamaño del archivo
            file_size_mb = document.file_size / (1024 * 1024)
            if file_size_mb > MAX_FILE_SIZE_MB:
                await processing_message.edit_text(
                    f"⚠️ El archivo es demasiado grande ({file_size_mb:.1f}MB).\n"
                    f"Tamaño máximo permitido: {MAX_FILE_SIZE_MB}MB"
                )
                return
            
            # Descargar archivo
            document_file = await context.bot.get_file(document.file_id)
            temp_file_path = self.temp_dir / f"document_{update.message.message_id}.{file_extension}"
            await document_file.download_to_drive(temp_file_path)
            
            # Transcribir
            transcription = await self.transcribe_audio(str(temp_file_path), file_extension)
            
            if transcription:
                # Enviar transcripción
                response_message = f"📝 *Transcripción:*\n\n{transcription}"
                await processing_message.edit_text(
                    response_message,
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await processing_message.edit_text(
                    "⚠️ No pude transcribir el audio. \n"
                    "Asegúrate de que el audio tenga buena calidad y esté en español."
                )
                
        except Exception as e:
            logger.error(f"Error procesando documento: {e}")
            await update.message.reply_text(
                "⚠️ Ocurrió un error al procesar el archivo. \n"
                "Por favor, inténtalo de nuevo."
            )
    
    async def handle_unknown_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Manejar mensajes no reconocidos"""
        await update.message.reply_text(
            "🤔 No reconozco este tipo de mensaje.\n\n"
            "Envíame:\n"
            "• Un mensaje de voz\n"
            "• Un archivo de audio\n"
            "• Usa /help para más información"
        )

def main():
    """Función principal"""
    # Verificar que estén configuradas las variables de entorno
    if not TELEGRAM_BOT_TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN no está configurado")
        return
    
    if not OPENAI_API_KEY:
        logger.error("OPENAI_API_KEY no está configurado")
        return
    
    # Crear instancia del bot
    bot = TranscriptionBot()
    
    # Crear aplicación
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Agregar handlers
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("info", bot.info_command))
    
    # Handlers para diferentes tipos de mensajes
    application.add_handler(MessageHandler(filters.VOICE, bot.handle_voice_message))
    application.add_handler(MessageHandler(filters.AUDIO, bot.handle_audio_file))
    application.add_handler(MessageHandler(filters.Document.ALL, bot.handle_document))
    
    # Handler para mensajes no reconocidos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bot.handle_unknown_message))
    
    # Iniciar el bot
    logger.info("Iniciando bot de transcripción...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

