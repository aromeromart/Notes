# Sistema de Telegram para PowerShell

*Creado el 16 de junio de 2025*

## 📱 Resumen

Se ha implementado un sistema completo para enviar mensajes a Telegram desde PowerShell usando la API oficial de bots. Este sistema permite automatizar notificaciones y comunicaciones desde scripts y comandos de terminal.

---

## 🎯 Funciones Implementadas

### **Funciones principales:**
- **`t "mensaje"`** - Envío rápido (alias principal)
- **`Send-TelegramMessage`** - Función completa con opciones avanzadas
- **`Set-TelegramCredentials`** - Configuración de credenciales
- **`telegramhelp`** - Ayuda completa del sistema

### **Ubicación:**
Todas las funciones están integradas en:
```
C:\Users\arome\OneDrive\OLD\Documentos\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

---

## 🔧 Configuración Inicial

### **Paso 1: Crear Bot de Telegram**
1. Abre Telegram y busca **@BotFather**
2. Envía `/newbot` y sigue las instrucciones
3. Elige un nombre para tu bot (ej: "MiBot PowerShell")
4. Elige un username que termine en "bot" (ej: "mipowershell_bot")
5. **Guarda el token** que te proporciona BotFather

### **Paso 2: Obtener Chat ID**
1. Envía un mensaje a tu bot recién creado
2. Visita en el navegador: `https://api.telegram.org/bot[TU_TOKEN]/getUpdates`
3. Busca en la respuesta JSON: `"chat":{"id":123456789}`
4. **Guarda ese número** como tu Chat ID

### **Paso 3: Configurar Credenciales**
```powershell
# Recargar perfil (si es necesario)
. $PROFILE

# Configurar credenciales
Set-TelegramCredentials -BotToken "1234567890:ABCDEF..." -ChatId "123456789"
```

---

## 🚀 Uso del Sistema

### **Envío rápido con alias `t`:**
```powershell
# Mensaje básico
t "Hola desde PowerShell!"

# Mensaje silencioso (sin notificación)
t "El backup ha terminado" -Silent

# Mensaje con formato Markdown
t "*Importante:* El proceso ha _terminado_ correctamente" -Markdown
```

### **Función completa `Send-TelegramMessage`:**
```powershell
# Mensaje con todas las opciones
Send-TelegramMessage -Message "Estado del servidor" -ParseMode "HTML" -Silent -DisableWebPagePreview

# Mensaje a chat específico
Send-TelegramMessage -Message "Hola" -ChatId "otro_chat_id"
```

---

## ⚙️ Parámetros Disponibles

### **Función `t` (Send-QuickTelegram):**
- `-Message` (obligatorio): Texto del mensaje
- `-Silent`: Envío sin notificación
- `-Markdown`: Aplicar formato Markdown

### **Función `Send-TelegramMessage` (completa):**
- `-Message` (obligatorio): Texto del mensaje
- `-BotToken` (opcional): Token específico (usa variable de entorno por defecto)
- `-ChatId` (opcional): Chat ID específico (usa variable de entorno por defecto)
- `-Silent`: Envío sin notificación
- `-ParseMode`: "Markdown", "HTML" o "MarkdownV2"
- `-DisableWebPagePreview`: Desactivar vista previa de enlaces

### **Función `Set-TelegramCredentials`:**
- `-BotToken` (obligatorio): Token del bot de Telegram
- `-ChatId` (obligatorio): ID del chat de destino

---

## 📝 Ejemplos Prácticos

### **Notificaciones de scripts:**
```powershell
# Al inicio de un proceso largo
t "Iniciando backup del servidor..."

# Al finalizar
t "✅ Backup completado a las $(Get-Date -Format 'HH:mm')" -Silent

# En caso de error
t "❌ Error en el backup: $($Error[0].Exception.Message)"
```

### **Monitoreo del sistema:**
```powershell
# Estado de procesos
$processes = Get-Process | Where-Object CPU -gt 50
if ($processes.Count -gt 0) {
    t "⚠️ Procesos con alta CPU: $($processes.Count)"
}

# Estado de disco
$freeSpace = (Get-WmiObject -Class Win32_LogicalDisk -Filter "DeviceID='C:'").FreeSpace / 1GB
if ($freeSpace -lt 10) {
    t "💾 Espacio en disco C: crítico: $([math]::Round($freeSpace, 2)) GB"
}
```

### **Mensajes con formato:**
```powershell
# Markdown
t "*Estado*: _Activo_\n\`\`\`\nServidor: OK\nDB: OK\n\`\`\`" -Markdown

# HTML (usando función completa)
Send-TelegramMessage -Message "<b>Alerta</b>: Sistema al <i>90%</i> de capacidad" -ParseMode "HTML"
```

---

## 🛡️ Seguridad y Privacidad

### **Almacenamiento de credenciales:**
- Las credenciales se guardan como **variables de entorno del usuario**
- Solo accesibles desde tu cuenta de Windows
- Persisten entre sesiones de PowerShell
- No se envían a terceros

### **Funcionamiento:**
- Utiliza la **API oficial de Telegram**
- No requiere acceso a cuenta personal
- Comunicación directa con servidores de Telegram
- Sin intermediarios o servicios externos

### **Buenas prácticas:**
- Mantén el token del bot seguro
- No compartas el token en código público
- Revoca el token si se compromete (via @BotFather)
- Usa mensajes silenciosos para notificaciones automáticas

---

## 🔍 Solución de Problemas

### **Error: "Token del bot no configurado"**
```powershell
# Verificar variables de entorno
$env:TELEGRAM_BOT_TOKEN
$env:TELEGRAM_CHAT_ID

# Reconfigurar si es necesario
Set-TelegramCredentials -BotToken "tu_token" -ChatId "tu_chat_id"
```

### **Error: "Chat ID no configurado"**
- Verifica que hayas enviado al menos un mensaje a tu bot
- Comprueba el Chat ID usando getUpdates
- Asegúrate de usar el Chat ID correcto (puede ser negativo para grupos)

### **Mensaje no llega:**
- Verifica que el bot esté activo
- Comprueba tu conexión a internet
- Revisa que el token sea correcto
- Confirma que el Chat ID sea válido

### **Error de curl:**
- Verifica que curl esté instalado (incluido en Windows 10+)
- Comprueba la conexión a internet
- Revisa que no haya firewall bloqueando

---

## 📚 Recursos Adicionales

### **Documentación oficial:**
- [Bot API de Telegram](https://core.telegram.org/bots/api)
- [Creación de bots con BotFather](https://core.telegram.org/bots#creating-a-new-bot)
- [Formato de mensajes Markdown](https://core.telegram.org/bots/api#markdown-style)

### **Comandos de ayuda:**
```powershell
# Mostrar ayuda completa
telegramhelp

# Verificar configuración
$env:TELEGRAM_BOT_TOKEN
$env:TELEGRAM_CHAT_ID
```

---

## 🔄 Estado del Proyecto

### **✅ Implementado:**
- Sistema completo de funciones de Telegram
- Integración en perfil de PowerShell
- Gestión de credenciales como variables de entorno
- Alias `t` para uso rápido
- Documentación completa
- Validación de respuestas de API
- Soporte para formato Markdown/HTML
- Mensajes silenciosos

### **⏳ Pendiente:**
- Configuración inicial del bot (requiere acción manual del usuario)
- Pruebas de funcionamiento
- Posibles mejoras según uso real

### **❌ No implementado (por diseño):**
- Acceso directo a cuenta personal de Telegram
- Envío a números de teléfono sin configuración previa
- Lectura de mensajes entrantes
- Gestión de grupos/canales sin permisos específicos

---

## 💡 Casos de Uso Recomendados

1. **Notificaciones de scripts automáticos**
2. **Monitoreo de sistemas**
3. **Alertas de procesos críticos**
4. **Confirmaciones de backups**
5. **Estados de deployments**
6. **Alertas de seguridad**
7. **Recordatorios y tareas**
8. **Integración con otros sistemas de automatización**

---

*Documento creado automáticamente el $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")*  
*Sistema integrado en perfil PowerShell: Microsoft.PowerShell_profile.ps1*  
*Versión: 1.0*

