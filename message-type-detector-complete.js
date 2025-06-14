// Message Type Detector - Código JavaScript Completo
// Configuración: Run Once for Each Item
// Lenguaje: JavaScript

const message = $json.message || $json.edited_message;

if (!message) {
  // Si no hay mensaje, devolver el elemento original sin cambios
  return $json;
}

// Detectar TODOS los tipos presentes (pueden ser múltiples)
const messageTypes = [];

// Verificar cada tipo posible en orden de prioridad
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
  primaryType = messageTypes[0]; // Usar el primero detectado (mayor prioridad)
}

// Detectar comandos especiales
if (primaryType === 'text' && message.text && message.text.startsWith('/')) {
  primaryType = 'command';
}

// Extraer información adicional útil
const additionalInfo = {};

// Si es texto, extraer el contenido
if (message.text) {
  additionalInfo.textContent = message.text;
  additionalInfo.textLength = message.text.length;
}

// Si es comando, extraer el comando específico
if (primaryType === 'command' && message.text) {
  additionalInfo.command = message.text.split(' ')[0]; // /start, /help, etc.
  additionalInfo.commandArgs = message.text.split(' ').slice(1); // argumentos
}

// Si tiene caption
if (message.caption) {
  additionalInfo.caption = message.caption;
  additionalInfo.captionLength = message.caption.length;
}

// Información del usuario
const userInfo = {};
if (message.from) {
  userInfo.userId = message.from.id;
  userInfo.firstName = message.from.first_name;
  userInfo.lastName = message.from.last_name || '';
  userInfo.username = message.from.username || '';
  userInfo.languageCode = message.from.language_code || 'en';
  userInfo.isBot = message.from.is_bot || false;
}

// Información del chat
const chatInfo = {};
if (message.chat) {
  chatInfo.chatId = message.chat.id;
  chatInfo.chatType = message.chat.type; // private, group, supergroup, channel
  chatInfo.chatTitle = message.chat.title || '';
}

// Timestamp del mensaje
const messageInfo = {
  messageId: message.message_id,
  date: message.date,
  timestamp: new Date(message.date * 1000).toISOString()
};

// Devolver resultado completo con toda la información
return {
  ...$json,
  messageType: primaryType,
  allMessageTypes: messageTypes,
  hasMultipleTypes: messageTypes.length > 1,
  isCommand: primaryType === 'command',
  additionalInfo: additionalInfo,
  userInfo: userInfo,
  chatInfo: chatInfo,
  messageInfo: messageInfo,
  isPrivateChat: chatInfo.chatType === 'private',
  isGroupChat: ['group', 'supergroup'].includes(chatInfo.chatType),
  isChannelPost: chatInfo.chatType === 'channel',
  hasText: messageTypes.includes('text') || !!message.caption,
  hasMedia: messageTypes.some(type => ['photo', 'video', 'audio', 'voice', 'document', 'sticker', 'animation'].includes(type)),
  debug: {
    detectedFields: Object.keys(message),
    processingTime: new Date().toISOString()
  }
};

