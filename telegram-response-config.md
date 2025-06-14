# Configuración de Respuesta Telegram

## Flujo Recomendado

```
Message Type Detector (Python) → Set Node → Telegram Response
```

## Nodo Set - Preparar Respuesta

### Configuración del Set Node:

**Assignments:**

1. **chatId** (Number)
   ```
   {{ $json.items[0].chatInfo.chatId }}
   ```

2. **messageType** (String)
   ```
   {{ $json.messageType }}
   ```

3. **userName** (String)
   ```
   {{ $json.items[0].userInfo.firstName }} {{ $json.items[0].userInfo.lastName }}
   ```

4. **response** (String)
   ```
   🤖 Mensaje procesado exitosamente!

📝 **Tipo detectado:** {{ $json.messageType }}
👤 **Usuario:** {{ $json.items[0].userInfo.firstName }}
📊 **Total procesados:** {{ $json.totalProcessed }}

✅ El mensaje fue clasificado correctamente.
   ```

## Respuesta Personalizada por Tipo

### Para respuesta dinámica según tipo:

**response** (String):
```javascript
{{
  $json.messageType === 'text' ? '📝 Mensaje de texto recibido: ' + $json.items[0].additionalInfo.textContent :
  $json.messageType === 'photo' ? '📸 Imagen recibida correctamente' :
  $json.messageType === 'voice' ? '🎤 Mensaje de voz procesado' :
  $json.messageType === 'document' ? '📄 Documento recibido y analizado' :
  $json.messageType === 'poll' ? '📊 Encuesta recibida: "' + $json.items[0].message.poll.question + '"' :
  $json.messageType === 'command' ? '⚙️ Comando ejecutado: ' + $json.items[0].additionalInfo.command :
  '✨ Tipo de mensaje: ' + $json.messageType + ' procesado correctamente'
}}
```

## Ejemplo Específico para tu Poll

### Set Node para Poll:

1. **chatId** (Number)
   ```
   {{ $json.items[0].chatInfo.chatId }}
   ```

2. **pollQuestion** (String)
   ```
   {{ $json.items[0].message.poll.question }}
   ```

3. **pollType** (String)
   ```
   {{ $json.items[0].message.poll.type }}
   ```

4. **totalOptions** (Number)
   ```
   {{ $json.items[0].message.poll.options.length }}
   ```

5. **response** (String)
   ```
   📊 **Encuesta Recibida**

**Pregunta:** {{ $json.items[0].message.poll.question }}
**Tipo:** {{ $json.items[0].message.poll.type === 'quiz' ? 'Quiz 🧠' : 'Encuesta regular 📊' }}
**Número de opciones:** {{ $json.items[0].message.poll.options.length }}
**Estado:** {{ $json.items[0].message.poll.is_closed ? 'Cerrada 🔒' : 'Abierta 🔓' }}

✅ La encuesta ha sido procesada correctamente por el sistema.
   ```

## Nodo Telegram Response

### Configuración:

- **Chat ID:** `{{ $json.chatId }}`
- **Text:** `{{ $json.response }}`
- **Parse Mode:** `Markdown` (opcional, para formato)

## JSON Completo del Set Node (para Poll)

```json
{
  "parameters": {
    "assignments": {
      "assignments": [
        {
          "id": "chatId",
          "name": "chatId",
          "value": "={{ $json.items[0].chatInfo.chatId }}",
          "type": "number"
        },
        {
          "id": "messageType",
          "name": "messageType",
          "value": "={{ $json.messageType }}",
          "type": "string"
        },
        {
          "id": "pollQuestion",
          "name": "pollQuestion",
          "value": "={{ $json.items[0].message.poll.question }}",
          "type": "string"
        },
        {
          "id": "response",
          "name": "response",
          "value": "📊 **Encuesta Recibida**\n\n**Pregunta:** {{ $json.items[0].message.poll.question }}\n**Tipo:** {{ $json.items[0].message.poll.type === 'quiz' ? 'Quiz 🧠' : 'Encuesta regular 📊' }}\n**Opciones:** {{ $json.items[0].message.poll.options.length }}\n\n✅ Procesado correctamente.",
          "type": "string"
        }
      ]
    }
  }
}
```

## Flujo Alternativo: Switch + Handlers Específicos

```
Message Type Detector → Switch Node
                        ├── poll → Poll Handler → Telegram
                        ├── text → Text Handler → Telegram  
                        ├── photo → Photo Handler → Telegram
                        └── default → Generic Handler → Telegram
```

### Ventajas del Switch:
- **Respuestas personalizadas** por tipo
- **Lógica específica** para cada tipo de mensaje
- **Escalabilidad** fácil

## Testing

### Para probar tu Poll:
1. **Envía la encuesta** al bot
2. **Verifica logs** del detector Python
3. **Comprueba la respuesta** del bot

### Respuesta esperada:
```
📊 Encuesta Recibida

Pregunta: dd
Tipo: Quiz 🧠
Opciones: 3

✅ Procesado correctamente.
```

---

**Recomendación:** Usa el **Set Node + Telegram** para empezar, y luego evoluciona al **Switch + Handlers** para más complejidad.

