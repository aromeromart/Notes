# Nodo Detector de Tipo de Mensaje

## Propósito
Nodo **Code** especializado exclusivamente en determinar el tipo de mensaje recibido de Telegram.

## Entrada
Recibe el JSON crudo del webhook de Telegram.

## Salida
Devuelve el mensaje original + un campo `messageType` simple.

## Código del Nodo

```javascript
// Nodo Code: Message Type Detector
const items = $input.all();
const output = [];

for (const item of items) {
  const message = item.json.message || item.json.edited_message;
  
  if (!message) {
    // Si no hay mensaje, skip
    continue;
  }
  
  // Determinar tipo de mensaje
  let messageType = 'unknown';
  
  if (message.text) {
    messageType = 'text';
  } else if (message.photo) {
    messageType = 'photo';
  } else if (message.video) {
    messageType = 'video';
  } else if (message.voice) {
    messageType = 'voice';
  } else if (message.audio) {
    messageType = 'audio';
  } else if (message.document) {
    messageType = 'document';
  } else if (message.sticker) {
    messageType = 'sticker';
  } else if (message.location) {
    messageType = 'location';
  } else if (message.contact) {
    messageType = 'contact';
  } else if (message.animation) {
    messageType = 'animation';
  } else if (message.video_note) {
    messageType = 'video_note';
  } else if (message.poll) {
    messageType = 'poll';
  } else if (message.dice) {
    messageType = 'dice';
  } else if (message.venue) {
    messageType = 'venue';
  } else if (message.game) {
    messageType = 'game';
  }
  
  // Añadir el tipo al mensaje original
  const result = {
    ...item.json,
    messageType: messageType
  };
  
  output.push({ json: result });
}

return output;
```

## Versión Simplificada (Solo tipos básicos)

```javascript
// Versión simple - Solo tipos esenciales
const items = $input.all();
const output = [];

for (const item of items) {
  const message = item.json.message || item.json.edited_message;
  
  if (!message) continue;
  
  let messageType = 'unknown';
  
  // Solo tipos principales
  if (message.text) {
    messageType = 'text';
  } else if (message.photo) {
    messageType = 'photo';
  } else if (message.voice) {
    messageType = 'voice';
  } else if (message.document) {
    messageType = 'document';
  } else if (message.video) {
    messageType = 'video';
  }
  
  output.push({ 
    json: {
      ...item.json,
      messageType: messageType
    }
  });
}

return output;
```

## Entrada de Ejemplo

```json
{
  "update_id": 123456789,
  "message": {
    "message_id": 1234,
    "from": {
      "id": 987654321,
      "first_name": "Juan"
    },
    "chat": {
      "id": 987654321,
      "type": "private"
    },
    "date": 1672531200,
    "text": "Hola bot"
  }
}
```

## Salida del Nodo

```json
{
  "update_id": 123456789,
  "message": {
    "message_id": 1234,
    "from": {
      "id": 987654321,
      "first_name": "Juan"
    },
    "chat": {
      "id": 987654321,
      "type": "private"
    },
    "date": 1672531200,
    "text": "Hola bot"
  },
  "messageType": "text"
}
```

## Casos de Uso

Después de este nodo, puedes usar un **Switch** para dirigir el flujo:

```
Telegram Trigger → Message Type Detector → Switch Node
                                            ├── text → Procesador de texto
                                            ├── photo → Procesador de imágenes
                                            ├── voice → Procesador de voz
                                            ├── document → Procesador de docs
                                            └── unknown → Handler por defecto
```

## Configuración del Switch Node

**Condiciones del Switch:**
- `{{ $json.messageType }}` equals `text`
- `{{ $json.messageType }}` equals `photo`
- `{{ $json.messageType }}` equals `voice`
- `{{ $json.messageType }}` equals `document`
- `{{ $json.messageType }}` equals `video`
- **Default**: Todos los demás casos

## Tipos Detectados

### ✅ Tipos Principales
- `text` - Mensaje de texto
- `photo` - Imagen/foto
- `voice` - Mensaje de voz
- `document` - Documento
- `video` - Video

### ✅ Tipos Adicionales (versión completa)
- `audio` - Audio
- `sticker` - Sticker
- `location` - Ubicación
- `contact` - Contacto
- `animation` - GIF
- `video_note` - Video circular
- `poll` - Encuesta
- `dice` - Dado
- `venue` - Lugar
- `game` - Juego

### ❓ Casos Especiales
- `unknown` - Tipo no identificado

## Testing

### Test Cases
1. **Texto**: `"Hola"` → `messageType: "text"`
2. **Foto**: Enviar imagen → `messageType: "photo"`
3. **Voz**: Grabar audio → `messageType: "voice"`
4. **Documento**: Subir PDF → `messageType: "document"`
5. **Video**: Enviar video → `messageType: "video"`

### Verificación
En n8n, añade un nodo **Set** después para verificar:
- `{{ $json.messageType }}` debería mostrar el tipo detectado

## Ventajas de este Enfoque

✅ **Simple**: Solo hace una cosa
✅ **Rápido**: Mínimo procesamiento
✅ **Claro**: Fácil de debuggear
✅ **Escalable**: Fácil añadir nuevos tipos
✅ **Reutilizable**: Se puede usar en cualquier flujo

---

**Siguiente paso**: Conectar a un Switch Node para dirigir el flujo según el tipo.

