# Set Node - Configuración Manual para Notificación

## Nombre del Nodo: "Message Received Notification"

## Assignments (6 campos):

### 1. **chatId** (Number)
**Value:**
```
{{ $json.items[0].chatInfo.chatId }}
```

### 2. **messageType** (String)
**Value:**
```
{{ $json.messageType }}
```

### 3. **userName** (String)
**Value:**
```
{{ $json.items[0].userInfo.firstName }} {{ $json.items[0].userInfo.lastName }}
```

### 4. **timestamp** (String)
**Value:**
```
{{ $json.items[0].messageInfo.timestamp }}
```

### 5. **hasMultipleTypes** (Boolean)
**Value:**
```
{{ $json.items[0].hasMultipleTypes }}
```

### 6. **response** (String)
**Value:**
```
🤖 **Mensaje Recibido y Procesado**

📝 **Tipo:** {{ $json.messageType }}{{ $json.items[0].hasMultipleTypes ? ' (múltiples tipos detectados)' : '' }}
👤 **De:** {{ $json.items[0].userInfo.firstName }} {{ $json.items[0].userInfo.lastName }}
🕐 **Hora:** {{ $now.format('HH:mm:ss') }}
📊 **ID Mensaje:** {{ $json.items[0].messageInfo.messageId }}

{{ $json.messageType === 'text' ? '💬 Texto: "' + $json.items[0].additionalInfo.textContent + '"' : $json.messageType === 'photo' ? '📸 Imagen recibida' : $json.messageType === 'video' ? '🎥 Video recibido' : $json.messageType === 'voice' ? '🎤 Mensaje de voz' : $json.messageType === 'audio' ? '🎵 Audio recibido' : $json.messageType === 'document' ? '📄 Documento: ' + ($json.items[0].message.document.file_name || 'Sin nombre') : $json.messageType === 'sticker' ? '😊 Sticker enviado' : $json.messageType === 'location' ? '📍 Ubicación compartida' : $json.messageType === 'contact' ? '👥 Contacto compartido' : $json.messageType === 'poll' ? '📊 Encuesta: "' + $json.items[0].message.poll.question + '"' : $json.messageType === 'command' ? '⚙️ Comando: ' + $json.items[0].additionalInfo.command : '✨ Contenido de tipo: ' + $json.messageType }}

✅ **Estado:** Procesado correctamente
```

## Nodo Telegram (después del Set)

### Configuración:
- **Chat ID:** `{{ $json.chatId }}`
- **Text:** `{{ $json.response }}`
- **Parse Mode:** `Markdown`

## Ejemplos de Respuestas

### Para tu Poll:
```
🤖 Mensaje Recibido y Procesado

📝 Tipo: poll
👤 De: Andrés Romero
🕐 Hora: 12:41:23
📊 ID Mensaje: 346

📊 Encuesta: "dd"

✅ Estado: Procesado correctamente
```

### Para Texto:
```
🤖 Mensaje Recibido y Procesado

📝 Tipo: text
👤 De: Andrés Romero
🕐 Hora: 12:41:23
📊 ID Mensaje: 347

💬 Texto: "Hola bot!"

✅ Estado: Procesado correctamente
```

### Para Comando:
```
🤖 Mensaje Recibido y Procesado

📝 Tipo: command
👤 De: Andrés Romero
🕐 Hora: 12:41:23
📊 ID Mensaje: 348

⚙️ Comando: /start

✅ Estado: Procesado correctamente
```

### Para Imagen:
```
🤖 Mensaje Recibido y Procesado

📝 Tipo: photo
👤 De: Andrés Romero
🕐 Hora: 12:41:23
📊 ID Mensaje: 349

📸 Imagen recibida

✅ Estado: Procesado correctamente
```

## Flujo Completo

```
Message Type Detector (Python) → Set Node (Notification) → Telegram Response
```

## Pasos para Implementar:

1. **Añadir Set Node** después del detector Python
2. **Configurar los 6 assignments** arriba
3. **Añadir Telegram Node** después del Set
4. **Configurar Telegram** con `chatId` y `response`
5. **Probar** enviando diferentes tipos de mensajes

---

**Este Set te dará información completa de todo lo que reciba el bot con un formato bonito y emojis!** 🚀

