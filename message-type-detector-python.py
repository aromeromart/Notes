# Message Type Detector - Python Code for n8n
# Nodo Code configurado para usar Python en lugar de JavaScript

# Obtener todos los elementos de entrada
items = _input.all()
output = []

# Procesar cada elemento
for item in items:
    # Obtener el mensaje del JSON
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if not message:
        # Si no hay mensaje, saltar este elemento
        continue
    
    # Inicializar tipo de mensaje como desconocido
    message_type = 'unknown'
    
    # Detectar tipo de mensaje - orden de prioridad
    if 'text' in message:
        message_type = 'text'
    elif 'photo' in message:
        message_type = 'photo'
    elif 'video' in message:
        message_type = 'video'
    elif 'voice' in message:
        message_type = 'voice'
    elif 'audio' in message:
        message_type = 'audio'
    elif 'document' in message:
        message_type = 'document'
    elif 'sticker' in message:
        message_type = 'sticker'
    elif 'animation' in message:
        message_type = 'animation'
    elif 'location' in message:
        message_type = 'location'
    elif 'contact' in message:
        message_type = 'contact'
    elif 'venue' in message:
        message_type = 'venue'
    elif 'poll' in message:
        message_type = 'poll'
    elif 'dice' in message:
        message_type = 'dice'
    elif 'game' in message:
        message_type = 'game'
    elif 'video_note' in message:
        message_type = 'video_note'
    
    # Crear el resultado combinando el JSON original con el tipo detectado
    result = item['json'].copy()  # Copiar el JSON original
    result['messageType'] = message_type  # Añadir el tipo detectado
    
    # Añadir al output
    output.append({'json': result})

# Retornar el resultado
return output

