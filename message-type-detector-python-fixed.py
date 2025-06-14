# Message Type Detector - Python para n8n (Formato Corregido)
# IMPORTANTE: Configurar el nodo en "Run Once for All Items"
# Lenguaje: Python

import json
from datetime import datetime

# Obtener todos los items
items = _input.all()

print(f"Recibidos {len(items)} items para procesar")

# Procesar cada item
processed_items = []

for item in items:
    # Obtener el mensaje del JSON
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if not message:
        # Si no hay mensaje, añadir el elemento original
        print('Item sin mensaje, saltando...')
        processed_items.append(dict(item['json']))
        continue
    
    print(f"Procesando mensaje ID: {message.get('message_id')}")
    
    # Detectar TODOS los tipos presentes
    message_types = []
    
    if 'text' in message:
        message_types.append('text')
    if 'photo' in message:
        message_types.append('photo')
    if 'video' in message:
        message_types.append('video')
    if 'voice' in message:
        message_types.append('voice')
    if 'audio' in message:
        message_types.append('audio')
    if 'document' in message:
        message_types.append('document')
    if 'sticker' in message:
        message_types.append('sticker')
    if 'animation' in message:
        message_types.append('animation')
    if 'location' in message:
        message_types.append('location')
    if 'contact' in message:
        message_types.append('contact')
    if 'venue' in message:
        message_types.append('venue')
    if 'poll' in message:
        message_types.append('poll')
    if 'dice' in message:
        message_types.append('dice')
    if 'game' in message:
        message_types.append('game')
    if 'video_note' in message:
        message_types.append('video_note')
    
    # Determinar tipo principal
    primary_type = 'unknown'
    if len(message_types) > 0:
        primary_type = message_types[0]
    
    # Detectar comandos
    if primary_type == 'text' and 'text' in message and message['text'].startswith('/'):
        primary_type = 'command'
    
    print(f"Tipo detectado: {primary_type}, todos los tipos: {', '.join(message_types)}")
    
    # Extraer información adicional
    additional_info = {}
    
    if 'text' in message:
        additional_info['textContent'] = message['text']
        additional_info['textLength'] = len(message['text'])
    
    if primary_type == 'command' and 'text' in message:
        text_parts = message['text'].split(' ')
        additional_info['command'] = text_parts[0]
        additional_info['commandArgs'] = text_parts[1:] if len(text_parts) > 1 else []
    
    if 'caption' in message:
        additional_info['caption'] = message['caption']
        additional_info['captionLength'] = len(message['caption'])
    
    # Información del usuario
    user_info = {}
    if 'from' in message:
        from_user = message['from']
        user_info['userId'] = from_user.get('id')
        user_info['firstName'] = from_user.get('first_name', '')
        user_info['lastName'] = from_user.get('last_name', '')
        user_info['username'] = from_user.get('username', '')
        user_info['languageCode'] = from_user.get('language_code', 'en')
        user_info['isBot'] = from_user.get('is_bot', False)
    
    # Información del chat
    chat_info = {}
    if 'chat' in message:
        chat = message['chat']
        chat_info['chatId'] = chat.get('id')
        chat_info['chatType'] = chat.get('type')
        chat_info['chatTitle'] = chat.get('title', '')
    
    # Timestamp del mensaje
    message_info = {
        'messageId': message.get('message_id'),
        'date': message.get('date'),
        'timestamp': datetime.fromtimestamp(message.get('date', 0)).isoformat() + 'Z'
    }
    
    # Crear resultado - COPIAR el JSON original y añadir nuevos campos
    result = dict(item['json'])
    
    # Añadir nuevos campos
    result.update({
        'messageType': primary_type,
        'allMessageTypes': message_types,
        'hasMultipleTypes': len(message_types) > 1,
        'isCommand': primary_type == 'command',
        'additionalInfo': additional_info,
        'userInfo': user_info,
        'chatInfo': chat_info,
        'messageInfo': message_info,
        'isPrivateChat': chat_info.get('chatType') == 'private',
        'isGroupChat': chat_info.get('chatType') in ['group', 'supergroup'],
        'isChannelPost': chat_info.get('chatType') == 'channel',
        'hasText': 'text' in message_types or 'caption' in message,
        'hasMedia': any(msg_type in ['photo', 'video', 'audio', 'voice', 'document', 'sticker', 'animation'] for msg_type in message_types),
        'debug': {
            'detectedFields': list(message.keys()),
            'processingTime': datetime.now().isoformat() + 'Z',
            'itemIndex': len(processed_items) + 1,
            'totalItems': len(items)
        }
    })
    
    processed_items.append(result)

print(f"Finalizando: {len(processed_items)} items procesados de {len(items)} recibidos")

# IMPORTANTE: En Python para n8n, devolver un diccionario con los items procesados
# Extraer el messageType del primer item para el nivel superior
first_message_type = 'unknown'
if processed_items and 'messageType' in processed_items[0]:
    first_message_type = processed_items[0]['messageType']

return {
    'messageType': first_message_type,  # messageType individual del primer mensaje
    'items': processed_items,
    'totalProcessed': len(processed_items),
    'totalReceived': len(items)
}

