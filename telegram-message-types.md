# Tipos de Mensajes en Telegram Bot API

## Mensajes de Contenido (Content Messages)

### 📝 Texto
- **`text`** - Mensaje de texto plano
- **`entities`** - Entidades en el texto (menciones, hashtags, URLs, etc.)

### 🖼️ Multimedia
- **`photo`** - Fotografías/imágenes
- **`video`** - Videos (archivos de video)
- **`video_note`** - Video mensajes circulares
- **`animation`** - GIFs animados
- **`audio`** - Archivos de audio
- **`voice`** - Mensajes de voz
- **`document`** - Documentos (PDF, DOC, etc.)
- **`sticker`** - Stickers/pegatinas

### 📍 Ubicación y Contacto
- **`location`** - Ubicación geográfica
- **`venue`** - Lugar específico (con nombre y dirección)
- **`contact`** - Información de contacto

### 🎲 Interactivos
- **`dice`** - Dados animados
- **`poll`** - Encuestas
- **`game`** - Juegos

## Mensajes del Sistema (System Messages)

### 👥 Gestión de Grupo
- **`new_chat_members`** - Nuevos miembros añadidos al grupo
- **`left_chat_member`** - Miembro que abandonó el grupo
- **`new_chat_title`** - Título del grupo cambiado
- **`new_chat_photo`** - Foto del grupo cambiada
- **`delete_chat_photo`** - Foto del grupo eliminada
- **`group_chat_created`** - Grupo creado
- **`supergroup_chat_created`** - Supergrupo creado
- **`channel_chat_created`** - Canal creado
- **`migrate_to_chat_id`** - Grupo migrado a supergrupo
- **`migrate_from_chat_id`** - Grupo migrado desde grupo normal
- **`pinned_message`** - Mensaje fijado

### 💰 Pagos (Payments)
- **`invoice`** - Factura de pago
- **`successful_payment`** - Pago exitoso

### 🔗 Servicios Conectados
- **`connected_website`** - Sitio web conectado
- **`passport_data`** - Datos de Telegram Passport

### 🎥 Video Chats
- **`video_chat_started`** - Video chat iniciado
- **`video_chat_ended`** - Video chat terminado
- **`video_chat_participants_invited`** - Participantes invitados al video chat
- **`video_chat_scheduled`** - Video chat programado

## Tipos de Actualizaciones (Update Types)

### 📨 Mensajes
- **`message`** - Mensaje nuevo
- **`edited_message`** - Mensaje editado
- **`channel_post`** - Publicación en canal
- **`edited_channel_post`** - Publicación de canal editada

### 🔘 Callbacks e Inline
- **`inline_query`** - Consulta inline
- **`chosen_inline_result`** - Resultado inline elegido
- **`callback_query`** - Callback de botón inline

### 📋 Otros
- **`shipping_query`** - Consulta de envío (pagos)
- **`pre_checkout_query`** - Pre-verificación de pago
- **`poll_answer`** - Respuesta a encuesta
- **`my_chat_member`** - Cambio en membresía del bot
- **`chat_member`** - Cambio en membresía de chat
- **`chat_join_request`** - Solicitud para unirse al chat

## Estructura por Tipo de Mensaje

### Mensaje de Texto
```json
{
  "message_id": 123,
  "from": { ... },
  "chat": { ... },
  "date": 1672531200,
  "text": "Hola mundo",
  "entities": [
    {
      "type": "mention",
      "offset": 0,
      "length": 8
    }
  ]
}
```

### Mensaje de Foto
```json
{
  "message_id": 124,
  "from": { ... },
  "chat": { ... },
  "date": 1672531200,
  "photo": [
    {
      "file_id": "AgACAgIAAxkBAAI...",
      "file_unique_id": "AQADBA...",
      "width": 1280,
      "height": 720,
      "file_size": 125000
    }
  ],
  "caption": "Descripción de la foto"
}
```

### Mensaje de Documento
```json
{
  "message_id": 125,
  "from": { ... },
  "chat": { ... },
  "date": 1672531200,
  "document": {
    "file_id": "BAADBAADbwADBRE...",
    "file_unique_id": "AgADbwAD...",
    "file_name": "documento.pdf",
    "mime_type": "application/pdf",
    "file_size": 1024000
  }
}
```

### Mensaje de Ubicación
```json
{
  "message_id": 126,
  "from": { ... },
  "chat": { ... },
  "date": 1672531200,
  "location": {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "live_period": 900,
    "heading": 90,
    "proximity_alert_radius": 100
  }
}
```

## Tipos de Entidades en Texto

### Formato
- **`bold`** - Texto en negrita
- **`italic`** - Texto en cursiva
- **`underline`** - Texto subrayado
- **`strikethrough`** - Texto tachado
- **`spoiler`** - Texto spoiler
- **`code`** - Código inline
- **`pre`** - Bloque de código

### Enlaces y Menciones
- **`url`** - URL
- **`text_link`** - Enlace de texto
- **`mention`** - Mención (@username)
- **`text_mention`** - Mención de usuario sin username
- **`hashtag`** - Hashtag (#tag)
- **`cashtag`** - Cashtag ($USD)
- **`bot_command`** - Comando de bot (/start)

### Datos
- **`email`** - Dirección de email
- **`phone_number`** - Número de teléfono

## Prioridades para el Agente IA

### 🔴 Alta Prioridad (Implementar primero)
- `text` - Mensajes de texto
- `photo` - Imágenes
- `document` - Documentos
- `voice` - Mensajes de voz
- `callback_query` - Botones inline

### 🟡 Media Prioridad (Fase 2)
- `video` - Videos
- `audio` - Audio
- `location` - Ubicaciones
- `contact` - Contactos
- `edited_message` - Mensajes editados

### 🟢 Baja Prioridad (Futuro)
- `sticker` - Stickers
- `animation` - GIFs
- `poll` - Encuestas
- `game` - Juegos
- Mensajes del sistema

## Detección en n8n

```javascript
function getMessageType(message) {
  // Orden de prioridad para detección
  if (message.text) return 'text';
  if (message.photo) return 'photo';
  if (message.video) return 'video';
  if (message.video_note) return 'video_note';
  if (message.voice) return 'voice';
  if (message.audio) return 'audio';
  if (message.document) return 'document';
  if (message.sticker) return 'sticker';
  if (message.animation) return 'animation';
  if (message.location) return 'location';
  if (message.venue) return 'venue';
  if (message.contact) return 'contact';
  if (message.poll) return 'poll';
  if (message.dice) return 'dice';
  if (message.game) return 'game';
  
  // Mensajes del sistema
  if (message.new_chat_members) return 'new_chat_members';
  if (message.left_chat_member) return 'left_chat_member';
  if (message.new_chat_title) return 'new_chat_title';
  if (message.pinned_message) return 'pinned_message';
  
  return 'unknown';
}
```

---

**Total aproximado**: **35+ tipos diferentes** de mensajes y actualizaciones

**Recomendación**: Empezar con los 5 tipos de alta prioridad y expandir gradualmente.

