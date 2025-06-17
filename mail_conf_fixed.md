# Configuración de Envío de Correos con PowerShell y Gmail

## 📋 Índice
- [Resumen del Proyecto](#resumen-del-proyecto)
- [Archivos Creados](#archivos-creados)
- [Funciones Disponibles](#funciones-disponibles)
- [Configuración Paso a Paso](#configuración-paso-a-paso)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Solución de Problemas](#solución-de-problemas)
- [Integración con Perfil PowerShell](#integración-con-perfil-powershell)

---

## 📝 Resumen del Proyecto

Se ha desarrollado un sistema completo de funciones PowerShell para enviar correos electrónicos usando Gmail SMTP. El sistema incluye:

- ✅ Autenticación segura con contraseñas de aplicación
- ✅ Envío de correos simples y con archivos adjuntos
- ✅ Soporte para HTML
- ✅ Manejo de errores con sugerencias
- ✅ Configuración persistente de credenciales
- ✅ Alias simplificados para uso rápido

---

## 📁 Archivos Creados

### `send-email.ps1`
**Ubicación:** `G:\Mi unidad\METANO-IA.ORG\code\Notes\send-email.ps1`

**Descripción:** Contiene todas las funciones necesarias para el envío de correos electrónicos.

**Funciones incluidas:**
- `Send-GmailMessage` - Función principal completa
- `Send-QuickMail` - Función simplificada (alias: `mail`)
- `Set-GmailCredentials` - Configuración de credenciales
- `Show-EmailHelp` - Ayuda y documentación (alias: `emailhelp`)

---

## 🔧 Funciones Disponibles

### 1. `Set-GmailCredentials`
**Propósito:** Configurar credenciales de Gmail de forma segura

```powershell
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "contraseña-aplicacion"
```

**Parámetros:**
- `Email` (Obligatorio): Dirección de Gmail
- `AppPassword` (Obligatorio): Contraseña de aplicación de Gmail

**Funcionalidad:**
- Guarda credenciales como variables de entorno del usuario
- Las credenciales persisten entre sesiones
- Configuración requerida solo una vez

### 2. `mail` (Alias de Send-QuickMail)
**Propósito:** Envío rápido de correos electrónicos

```powershell
mail -To "destino@email.com" -Subject "Asunto" -Body "Mensaje"
```

**Parámetros:**
- `To` (Obligatorio): Dirección de destino
- `Subject` (Obligatorio): Asunto del correo
- `Body` (Obligatorio): Contenido del mensaje
- `Attachments` (Opcional): Array de archivos adjuntos

### 3. `Send-GmailMessage`
**Propósito:** Función completa con todas las opciones avanzadas

```powershell
Send-GmailMessage -To "destino@email.com" -Subject "Asunto" -Body "Mensaje" -BodyAsHTML
```

**Parámetros completos:**
- `To` (Obligatorio): Dirección de destino
- `Subject` (Obligatorio): Asunto del correo
- `Body` (Obligatorio): Contenido del mensaje
- `Attachments` (Opcional): Array de archivos adjuntos
- `From` (Opcional): Dirección de origen (usa credenciales por defecto)
- `SmtpServer` (Opcional): Servidor SMTP (por defecto: smtp.gmail.com)
- `Port` (Opcional): Puerto SMTP (por defecto: 587)
- `BodyAsHTML` (Opcional): Switch para contenido HTML

### 4. `emailhelp` (Alias de Show-EmailHelp)
**Propósito:** Mostrar ayuda y documentación

```powershell
emailhelp
```

---

## ⚙️ Configuración Paso a Paso

### Paso 1: Habilitar Verificación en 2 Pasos en Gmail

1. Ve a **Google Account Security**: https://myaccount.google.com/security
2. En la sección "Iniciar sesión en Google", haz clic en "Verificación en 2 pasos"
3. Sigue las instrucciones para habilitar la verificación en 2 pasos
4. **⚠️ IMPORTANTE:** Sin este paso, no podrás generar contraseñas de aplicación

### Paso 2: Generar Contraseña de Aplicación

1. Ve a **App Passwords**: https://myaccount.google.com/apppasswords
2. En "Seleccionar app", elige "Correo" o "Otra (nombre personalizado)"
3. Si eliges "Otra", escribe "PowerShell" como nombre
4. Haz clic en "Generar"
5. **📋 Copia la contraseña de 16 caracteres** (formato: xxxx xxxx xxxx xxxx)
6. **⚠️ IMPORTANTE:** Esta contraseña solo se muestra una vez

### Paso 3: Cargar las Funciones

```powershell
# Cargar el script con las funciones
. "G:\Mi unidad\METANO-IA.ORG\code\Notes\send-email.ps1"
```

### Paso 4: Configurar Credenciales

```powershell
# Configurar credenciales (reemplaza con tus datos reales)
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "xxxx xxxx xxxx xxxx"
```

**Ejemplo real usado:**
```powershell
Set-GmailCredentials -Email "aromeromar@gmail.com" -AppPassword "olks ewkd mwjz jwgn"
```

### Paso 5: Verificar Configuración

```powershell
# Enviar correo de prueba
mail -To "aromeromar@gmail.com" -Subject "prueba desde ps" -Body "¡Funciona!"
```

---

## 📧 Ejemplos de Uso

### Envío Simple
```powershell
mail -To "destinatario@email.com" -Subject "Hola" -Body "Este es mi mensaje"
```

### Envío con Archivos Adjuntos
```powershell
mail -To "destinatario@email.com" -Subject "Documentos" -Body "Adjunto los archivos solicitados" -Attachments @("documento.pdf", "imagen.jpg")
```

### Envío con HTML
```powershell
Send-GmailMessage -To "destinatario@email.com" -Subject "Newsletter" -Body "<h1>Título</h1><p>Contenido en <b>HTML</b></p>" -BodyAsHTML
```

### Envío a Múltiples Destinatarios (usando bucle)
```powershell
$destinatarios = @("usuario1@email.com", "usuario2@email.com", "usuario3@email.com")
foreach ($dest in $destinatarios) {
    mail -To $dest -Subject "Mensaje masivo" -Body "Hola, este es un mensaje personalizado"
    Start-Sleep -Seconds 1  # Pausa de 1 segundo entre envíos
}
```

### Envío desde Archivo de Texto
```powershell
$mensaje = Get-Content "mensaje.txt" -Raw
mail -To "destinatario@email.com" -Subject "Mensaje desde archivo" -Body $mensaje
```

---

## 🔍 Solución de Problemas

### Error: "Authentication Required"

**Causa:** Contraseña incorrecta o no es una contraseña de aplicación

**Solución:**
1. Verifica que estés usando una **contraseña de aplicación**, no tu contraseña normal
2. Regenera la contraseña de aplicación si es necesario
3. Vuelve a configurar con `Set-GmailCredentials`

### Error: "SSL Connection"

**Causa:** Problemas de conexión SSL/TLS

**Solución:**
1. Verifica tu conexión a internet
2. Comprueba si tu firewall/antivirus bloquea la conexión
3. Intenta desde otra red si es posible

### Error: "Archivo no encontrado" (Adjuntos)

**Causa:** Ruta de archivo adjunto incorrecta

**Solución:**
```powershell
# Verifica que el archivo existe
Test-Path "ruta/al/archivo.pdf"

# Usa rutas absolutas
mail -To "dest@email.com" -Subject "Test" -Body "Test" -Attachments @("C:\Users\usuario\Desktop\archivo.pdf")
```

### Variables de Entorno no Persistentes

**Causa:** Las variables de entorno se pierden al cerrar PowerShell

**Solución:**
```powershell
# Verificar variables actuales
echo $env:GMAIL_USER
echo $env:GMAIL_APP_PASSWORD

# Reconfigurar si es necesario
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "tu-contraseña-app"
```

---

## 🔄 Integración con Perfil PowerShell

### ¿Qué es el Perfil PowerShell?
El perfil PowerShell es un script que se ejecuta automáticamente cada vez que inicias una nueva sesión de PowerShell, permitiendo cargar funciones personalizadas permanentemente.

### Ubicación del Perfil
```powershell
# Ver ruta del perfil
$PROFILE

# Verificar si existe
Test-Path $PROFILE
```

### Agregar Funciones al Perfil

**Opción 1: Cargar el script completo**
```powershell
# Agregar esta línea al perfil
. "G:\Mi unidad\METANO-IA.ORG\code\Notes\send-email.ps1"
```

**Opción 2: Copiar funciones directamente**
1. Abrir el perfil: `notepad $PROFILE`
2. Copiar el contenido completo de `send-email.ps1`
3. Guardar y recargar: `. $PROFILE`

### Verificar Carga de Funciones
```powershell
# Listar funciones cargadas
Get-Command mail, emailhelp, Set-GmailCredentials

# Probar ayuda
emailhelp
```

---

## 📊 Pruebas Realizadas

### Configuración Exitosa
✅ **Email configurado:** aromeromar@gmail.com  
✅ **Contraseña de aplicación:** olks ewkd mwjz jwgn  
✅ **Credenciales guardadas:** Variables de entorno del usuario  

### Envíos de Prueba Exitosos
✅ **Prueba 1:** aromeromar@gmail.com - "prueba desde ps"  
✅ **Prueba 2:** aromero@metano-ia.org - "prueba desde ps"  

### Funciones Verificadas
✅ `Set-GmailCredentials` - Configuración de credenciales  
✅ `mail` - Envío simple  
✅ `emailhelp` - Ayuda y documentación  
✅ Manejo de errores y sugerencias  

---

## 🚀 Comandos de Referencia Rápida

```powershell
# Cargar funciones
. "G:\Mi unidad\METANO-IA.ORG\code\Notes\send-email.ps1"

# Configurar credenciales (solo una vez)
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "xxxx xxxx xxxx xxxx"

# Enviar correo simple
mail -To "destino@email.com" -Subject "Asunto" -Body "Mensaje"

# Enviar con adjuntos
mail -To "destino@email.com" -Subject "Asunto" -Body "Mensaje" -Attachments @("archivo.pdf")

# Mostrar ayuda
emailhelp

# Verificar configuración
echo $env:GMAIL_USER
```

---

## 📝 Notas Adicionales

- **Seguridad:** Las contraseñas se almacenan como variables de entorno del usuario
- **Persistencia:** La configuración persiste entre sesiones de PowerShell
- **Compatibilidad:** Funciona con Windows PowerShell 5.1 y PowerShell Core
- **Gmail:** Funciona exclusivamente con cuentas de Gmail
- **Límites:** Gmail tiene límites de envío (500 correos/día para cuentas gratuitas)

---

**Documento creado:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")  
**Autor:** Sistema PowerShell  
**Versión:** 1.0

