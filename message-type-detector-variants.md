# Message Type Detector - Variaciones en Python

## Versión Básica (Solo tipos principales)

```python
# Message Type Detector - Versión Simplificada
items = _input.all()
output = []

for item in items:
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if not message:
        continue
    
    message_type = 'unknown'
    
    # Solo tipos principales
    if 'text' in message:
        message_type = 'text'
    elif 'photo' in message:
        message_type = 'photo'
    elif 'voice' in message:
        message_type = 'voice'
    elif 'document' in message:
        message_type = 'document'
    elif 'video' in message:
        message_type = 'video'
    
    result = item['json'].copy()
    result['messageType'] = message_type
    output.append({'json': result})

return output
```

## Versión con Funciones (Más organizada)

```python
# Message Type Detector - Versión con Funciones

def detect_message_type(message):
    """Detecta el tipo de mensaje de Telegram"""
    type_checks = [
        ('text', 'text'),
        ('photo', 'photo'),
        ('video', 'video'),
        ('voice', 'voice'),
        ('audio', 'audio'),
        ('document', 'document'),
        ('sticker', 'sticker'),
        ('animation', 'animation'),
        ('location', 'location'),
        ('contact', 'contact'),
        ('venue', 'venue'),
        ('poll', 'poll'),
        ('dice', 'dice'),
        ('game', 'game'),
        ('video_note', 'video_note')
    ]
    
    for field, msg_type in type_checks:
        if field in message:
            return msg_type
    
    return 'unknown'

# Código principal
items = _input.all()
output = []

for item in items:
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if message:
        message_type = detect_message_type(message)
        
        result = item['json'].copy()
        result['messageType'] = message_type
        output.append({'json': result})

return output
```

## Versión con Logging y Debug

```python
# Message Type Detector - Versión con Debug
import json

def detect_message_type_with_debug(message):
    """Detecta el tipo de mensaje con información de debug"""
    available_fields = list(message.keys())
    
    type_mapping = {
        'text': 'text',
        'photo': 'photo', 
        'video': 'video',
        'voice': 'voice',
        'audio': 'audio',
        'document': 'document',
        'sticker': 'sticker',
        'animation': 'animation',
        'location': 'location',
        'contact': 'contact',
        'venue': 'venue',
        'poll': 'poll',
        'dice': 'dice',
        'game': 'game',
        'video_note': 'video_note'
    }
    
    for field, msg_type in type_mapping.items():
        if field in message:
            return msg_type, available_fields
    
    return 'unknown', available_fields

# Código principal
items = _input.all()
output = []

for item in items:
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if message:
        message_type, debug_fields = detect_message_type_with_debug(message)
        
        result = item['json'].copy()
        result['messageType'] = message_type
        result['debugFields'] = debug_fields  # Para debugging
        
        output.append({'json': result})

return output
```

## Versión con Manejo de Comandos

```python
# Message Type Detector - Con detección de comandos

def detect_message_type_advanced(message):
    """Detecta tipo de mensaje con análisis avanzado"""
    
    # Detectar comandos primero
    if 'text' in message and message['text'].startswith('/'):
        return 'command'
    
    # Tipos de contenido
    content_types = [
        ('text', 'text'),
        ('photo', 'photo'),
        ('video', 'video'), 
        ('voice', 'voice'),
        ('audio', 'audio'),
        ('document', 'document'),
        ('sticker', 'sticker'),
        ('animation', 'animation'),
        ('location', 'location'),
        ('contact', 'contact'),
        ('venue', 'venue'),
        ('poll', 'poll'),
        ('dice', 'dice'),
        ('game', 'game'),
        ('video_note', 'video_note')
    ]
    
    for field, msg_type in content_types:
        if field in message:
            return msg_type
            
    return 'unknown'

# Código principal
items = _input.all()
output = []

for item in items:
    message = item['json'].get('message') or item['json'].get('edited_message')
    
    if message:
        message_type = detect_message_type_advanced(message)
        
        result = item['json'].copy()
        result['messageType'] = message_type
        
        # Añadir información adicional
        if message_type == 'command' and 'text' in message:
            result['command'] = message['text'].split()[0]  # Primer palabra
        
        output.append({'json': result})

return output
```

## Versión Compacta (Una línea por tipo)

```python
# Message Type Detector - Versión Ultra Compacta
items = _input.all()
output = []

types = ['text', 'photo', 'video', 'voice', 'audio', 'document', 
         'sticker', 'animation', 'location', 'contact', 'venue', 
         'poll', 'dice', 'game', 'video_note']

for item in items:
    msg = item['json'].get('message') or item['json'].get('edited_message')
    if msg:
        msg_type = next((t for t in types if t in msg), 'unknown')
        result = item['json'].copy()
        result['messageType'] = msg_type
        output.append({'json': result})

return output
```

## Configuración en n8n

### Para usar Python en el nodo Code:

1. **Crear nodo Code**
2. **Configurar Language**: Cambiar de JavaScript a **Python**
3. **Pegar código** de cualquiera de las versiones arriba
4. **Guardar y probar**

### Variables disponibles en n8n Python:

- `_input.all()` - Todos los elementos de entrada
- `_input.first()` - Primer elemento
- `item['json']` - Datos JSON del elemento
- `return output` - Devolver resultado

### Diferencias con JavaScript:

| JavaScript | Python |
|------------|--------|
| `$input.all()` | `_input.all()` |
| `item.json` | `item['json']` |
| `message.text` | `message['text']` |
| `...item.json` | `item['json'].copy()` |

## Recomendación

Usa la **Versión Básica** para empezar, y si necesitas más funcionalidades, puedes evolucionar a las versiones más avanzadas.

### Testing

Para probar el código:
1. Envía diferentes tipos de mensajes al bot
2. Verifica que `messageType` se detecte correctamente
3. Usa la versión con debug si hay problemas

