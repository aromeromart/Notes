# Message Type Detector - Versión Corregida

## Problema Identificado
El error `Can't use .all() here` ocurre cuando el nodo Code está configurado en modo "Run Once for Each Item" pero se usa `$input.all()`. 

## Solución: Dos Versiones del Código

### Versión 1: Run Once for Each Item (RECOMENDADA)

**Configuración del nodo:**
- **Mode**: `Run Once for Each Item`
- **Language**: `JavaScript`

```javascript
// Message Type Detector - Para "Run Once for Each Item"
// Esta versión procesa un elemento a la vez

const message = $json.message || $json.edited_message;

if (!message) {
  // Si no hay mensaje, devolver el elemento original sin cambios
  return $json;
}

// Detectar TODOS los tipos presentes (pueden ser múltiples)
const messageTypes = [];

// Verificar cada tipo posible
if (message.text) messageTypes.push('text');
if (message.photo) messageTypes.push('photo');
if (message.video) messageTypes.push('video');
if (message.voice) messageTypes.push('voice');
if (message.audio) messageTypes.push('audio');
if (message.document) messageTypes.push('document');
if (message.sticker) messageTypes.push('sticker');
if (message.animation) messageTypes.push('animation');
if (message.location) messageTypes.push('location');
if (message.contact) messageTypes.push('contact');
if (message.venue) messageTypes.push('venue');
if (message.poll) messageTypes.push('poll');
if (message.dice) messageTypes.push('dice');
if (message.game) messageTypes.push('game');
if (message.video_note) messageTypes.push('video_note');

// Determinar tipo principal con prioridad
let primaryType = 'unknown';
if (messageTypes.length > 0) {
  primaryType = messageTypes[0]; // Usar el primero detectado
}

// Detectar comandos especiales
if (primaryType === 'text' && message.text && message.text.startsWith('/')) {
  primaryType = 'command';
}

// Devolver resultado con información adicional
return {
  ...$json,
  messageType: primaryType,
  allMessageTypes: messageTypes,
  hasMultipleTypes: messageTypes.length > 1,
  isCommand: primaryType === 'command'
};
```

### Versión 2: Run Once for All Items

**Configuración del nodo:**
- **Mode**: `Run Once for All Items`
- **Language**: `JavaScript`

```javascript
// Message Type Detector - Para "Run Once for All Items"
// Esta versión procesa todos los elementos de una vez

const items = $input.all();
const output = [];

for (const item of items) {
  const message = item.json.message || item.json.edited_message;
  
  if (!message) {
    // Si no hay mensaje, añadir el elemento original
    output.push(item);
    continue;
  }
  
  // Detectar TODOS los tipos presentes
  const messageTypes = [];
  
  if (message.text) messageTypes.push('text');
  if (message.photo) messageTypes.push('photo');
  if (message.video) messageTypes.push('video');
  if (message.voice) messageTypes.push('voice');
  if (message.audio) messageTypes.push('audio');
  if (message.document) messageTypes.push('document');
  if (message.sticker) messageTypes.push('sticker');
  if (message.animation) messageTypes.push('animation');
  if (message.location) messageTypes.push('location');
  if (message.contact) messageTypes.push('contact');
  if (message.venue) messageTypes.push('venue');
  if (message.poll) messageTypes.push('poll');
  if (message.dice) messageTypes.push('dice');
  if (message.game) messageTypes.push('game');
  if (message.video_note) messageTypes.push('video_note');
  
  // Determinar tipo principal
  let primaryType = 'unknown';
  if (messageTypes.length > 0) {
    primaryType = messageTypes[0];
  }
  
  // Detectar comandos
  if (primaryType === 'text' && message.text && message.text.startsWith('/')) {
    primaryType = 'command';
  }
  
  const result = {
    ...item.json,
    messageType: primaryType,
    allMessageTypes: messageTypes,
    hasMultipleTypes: messageTypes.length > 1,
    isCommand: primaryType === 'command'
  };
  
  output.push({ json: result });
}

return output;
```

## Manejo de Mensajes Múltiples

### Casos donde pueden venir múltiples tipos:
1. **Foto + Caption**: `photo` + `text` (caption)
2. **Video + Caption**: `video` + `text`
3. **Document + Caption**: `document` + `text`
4. **Location + Venue**: `location` + `venue`

### Prioridades establecidas:
1. `text` (más alta prioridad)
2. `photo`
3. `video`
4. `voice`
5. `audio`
6. `document`
7. Resto de tipos...

## Switch Node Mejorado

Para manejar comandos, añadir una salida adicional:

```json
{
  "output": 16,
  "expression": "={{ $json.messageType === 'command' }}"
}
```

**Arquitectura actualizada:**
```
Switch Node (17 salidas)
├── 0: text
├── 1: photo
├── 2: video
...
├── 15: unknown
└── 16: command  (NUEVA)
```

## Debug y Troubleshooting

### Para verificar múltiples tipos:
```javascript
// Añadir al final del código
console.log('Detected types:', messageTypes);
console.log('Primary type:', primaryType);
console.log('Has multiple:', messageTypes.length > 1);
```

### Ejemplo de salida con múltiples tipos:
```json
{
  "messageType": "photo",
  "allMessageTypes": ["photo", "text"],
  "hasMultipleTypes": true,
  "isCommand": false,
  "message": {
    "photo": [...],
    "caption": "Esta es una foto"
  }
}
```

## Configuración Recomendada

1. **Usar Versión 1** (Run Once for Each Item) - es más eficiente
2. **Configurar Switch** con 17 salidas (incluyendo commands)
3. **Probar con mensajes mixtos** (foto + caption, video + texto, etc.)
4. **Monitorear** el campo `hasMultipleTypes` para casos especiales

## Testing

### Casos de prueba:
1. **Texto simple**: "Hola" → `messageType: "text"`
2. **Comando**: "/start" → `messageType: "command"`
3. **Foto con caption**: Imagen + "Mi foto" → `messageType: "photo", allMessageTypes: ["photo", "text"]`
4. **Documento con caption**: PDF + "Mi documento" → `messageType: "document", allMessageTypes: ["document", "text"]`

---

**Solución aplicada**: El error se resuelve usando la configuración correcta del nodo y evitando `.all()` cuando no es apropiado.

