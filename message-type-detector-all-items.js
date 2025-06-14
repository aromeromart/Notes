// Message Type Detector - Maneja Múltiples Items
// IMPORTANTE: Configurar el nodo en "Run Once for All Items"
// Lenguaje: JavaScript

const items = $input.all();
const output = [];

console.log(`Recibidos ${items.length} items para procesar`);

for (const item of items) {
  const message = item.json.message || item.json.edited_message;
  
  if (!message) {
    // Si no hay mensaje, añadir el elemento original
    console.log('Item sin mensaje, saltando...');
    output.push(item);
    continue;
  }
  
  console.log(`Procesando mensaje ID: ${message.message_id}`);
  
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
  
  console.log(`Tipo detectado: ${primaryType}, todos los tipos: ${messageTypes.join(', ')}`);
  
  // Extraer información adicional
  const additionalInfo = {};
  
  if (message.text) {
    additionalInfo.textContent = message.text;
    additionalInfo.textLength = message.text.length;
  }
  
  if (primaryType === 'command' && message.text) {
    additionalInfo.command = message.text.split(' ')[0];
    additionalInfo.commandArgs = message.text.split(' ').slice(1);
  }
  
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
    chatInfo.chatType = message.chat.type;
    chatInfo.chatTitle = message.chat.title || '';
  }
  
  // Timestamp del mensaje
  const messageInfo = {
    messageId: message.message_id,
    date: message.date,
    timestamp: new Date(message.date * 1000).toISOString()
  };
  
  // Crear resultado
  const result = {
    ...item.json,
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
      processingTime: new Date().toISOString(),
      itemIndex: output.length + 1,
      totalItems: items.length
    }
  };
  
  output.push({ json: result });
}

console.log(`Finalizando: ${output.length} items procesados de ${items.length} recibidos`);

return output;

