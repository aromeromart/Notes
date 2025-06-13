# Configuración Telegram Bot

## Bot Information
- **Bot Name**: [Tu nombre de bot]
- **Bot Username**: [tu_bot_username]
- **Bot Token**: `[MANTENER_SECRETO]`
- **Creation Date**: 2025-06-13

## n8n Trigger Configuration

### Telegram Trigger Node
```json
{
  "name": "Telegram Trigger",
  "type": "n8n-nodes-base.telegramTrigger",
  "parameters": {
    "authentication": "accessToken",
    "accessToken": "{{TELEGRAM_BOT_TOKEN}}",
    "updates": [
      "message",
      "edited_message",
      "callback_query"
    ],
    "additionalFields": {
      "download": true
    }
  }
}
```

### Pre-processing Code Node

**Propósito**: Limpiar y estructurar datos del webhook

**Salida esperada**:
```json
{
  "messageId": 123,
  "timestamp": "2025-06-13T20:46:23Z",
  "messageType": "text",
  "userId": 987654321,
  "userName": "Usuario",
  "userUsername": "username",
  "userLanguage": "es",
  "chatId": -123456789,
  "chatType": "private",
  "text": "Hola bot!",
  "isCommand": false,
  "isEdited": false
}
```

## Filtros Implementados

### Tipos de Mensaje Soportados
- ✅ **text** - Mensajes de texto
- ✅ **photo** - Imágenes
- ✅ **document** - Documentos
- ✅ **voice** - Mensajes de voz
- ✅ **video** - Videos
- ✅ **audio** - Audio
- ✅ **sticker** - Stickers
- ✅ **location** - Ubicación
- ❌ **unknown** - Otros tipos (filtrados)

### Validaciones
- ✅ Mensaje no vacío
- ✅ Usuario válido
- ✅ Chat ID presente
- ✅ Detección de comandos (`/start`, `/help`, etc.)
- ✅ Detección de mensajes editados

## Testing Checklist

### Tests básicos
- [ ] Bot responde a `/start`
- [ ] Recibe mensajes de texto
- [ ] Procesa imágenes
- [ ] Maneja comandos
- [ ] Detecta usuarios nuevos

### Tests avanzados
- [ ] Webhook funciona correctamente
- [ ] Metadatos se capturan bien
- [ ] Filtros funcionan
- [ ] Manejo de errores
- [ ] Rate limiting

## Comandos de Testing

```bash
# Verificar bot está activo
curl "https://api.telegram.org/bot<TOKEN>/getMe"

# Ver webhook info
curl "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"

# Eliminar webhook (si necesitas resetear)
curl "https://api.telegram.org/bot<TOKEN>/deleteWebhook"
```

## Próximos Pasos

1. ✅ **Telegram Trigger configurado**
2. ⏳ **Pre-procesamiento implementado**
3. ⏳ **Análisis de intención (siguiente fase)**
4. ⏳ **Router inteligente**
5. ⏳ **Módulos de respuesta**

## Notas de Seguridad

- 🔒 **Token del bot**: Nunca commitear en Git
- 🔒 **Webhook URL**: Usar HTTPS siempre
- 🔒 **Validación**: Verificar origen de mensajes
- 🔒 **Rate limiting**: Implementar límites por usuario

---

**Estado**: Configuración inicial  
**Última actualización**: 2025-06-13

