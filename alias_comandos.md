# Alias y Funciones Personalizados - PowerShell

*Generado el 16 de junio de 2025*

## Resumen

Este documento describe todas las funciones y alias personalizados definidos en tu perfil de PowerShell. Estas herramientas están diseñadas para mejorar tu productividad en tareas de desarrollo, gestión de notas, comunicación y transcripción de audio.

---

## 📁 Navegación y Git

### `g()`
**Descripción:** Abre el repositorio GitHub actual en Microsoft Edge  
**Uso:** `g`  
**Funcionalidad:**
- Detecta automáticamente la URL del repositorio git
- Convierte URLs SSH a HTTPS
- Abre el repositorio en el navegador

### `notes()`
**Descripción:** Navega rápidamente al directorio de notas  
**Uso:** `notes`  
**Destino:** `G:\Mi unidad\METANO-IA.ORG\code\Notes`

### `readme()`
**Descripción:** Abre README.md en Notepad++  
**Uso:** `readme`

---

## 📝 Gestión de Notas y Tareas

### `xx()`
**Descripción:** Busca y muestra todas las notas marcadas con "XX " en archivos .md  
**Uso:** `xx`  
**Funcionalidad:**
- Escanea todos los archivos .md del directorio actual
- Busca líneas que empiecen con "XX " o "xx "
- Muestra resumen con estadísticas
- Útil para encontrar tareas pendientes o notas importantes

**Ejemplo de salida:**
```
Archivo: proyecto.md
  Línea 15: Revisar documentación de API
  Línea 23: Contactar con el cliente

RESUMEN
Archivos analizados: 5
Archivos con notas: 2
Total de notas: 8
```

### `xxx([patrón], [archivo_salida])`
**Descripción:** Extrae notas marcadas y las mueve a un archivo específico  
**Uso:** 
- `xxx` - Extrae "XX " a pendientes.md
- `xxx "TODO " "tareas.md"` - Extrae "TODO " a tareas.md

**Funcionalidad:**
- Busca y extrae líneas que coincidan con el patrón
- Remueve las líneas de los archivos originales
- Las añade al archivo de destino
- Útil para consolidar tareas pendientes

### `x()`
**Descripción:** Abre o crea pendientes.md en el directorio actual  
**Uso:** `x`  
**Funcionalidad:**
- Si existe pendientes.md, lo abre en Notepad++
- Si no existe, pregunta si quieres crearlo
- Crea el archivo con plantilla básica

---

## 📧 Sistema de Correo Electrónico

### `mail -To <destino> -Subject <asunto> -Body <mensaje> [-Attachments <archivos>]`
**Descripción:** Envía emails rápidamente usando Gmail  
**Alias de:** `Send-QuickMail`

**Ejemplos:**
```powershell
# Email simple
mail -To "juan@ejemplo.com" -Subject "Hola" -Body "¿Cómo estás?"

# Con archivos adjuntos
mail -To "equipo@empresa.com" -Subject "Reporte" -Body "Adjunto el reporte" -Attachments @("reporte.pdf", "datos.xlsx")
```

### `Send-GmailMessage`
**Descripción:** Función completa para envío de emails con todas las opciones  
**Parámetros adicionales:**
- `-From` - Email remitente
- `-BodyAsHTML` - Enviar como HTML
- `-SmtpServer` - Servidor SMTP personalizado
- `-Port` - Puerto personalizado

### `Set-GmailCredentials -Email <email> -AppPassword <contraseña>`
**Descripción:** Configura credenciales de Gmail como variables de entorno  
**Uso:** `Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "app-password"`

### `emailhelp`
**Descripción:** Muestra ayuda completa del sistema de email  
**Alias de:** `Show-EmailHelp`

**Requisitos importantes:**
- Usar contraseña de aplicación (no la contraseña normal)
- Tener verificación en 2 pasos habilitada
- Generar contraseña en: https://myaccount.google.com/apppasswords

---

## 🎤 Transcripción de Audio (Speech-to-Text)

### `S2T <archivo_audio> [opciones]`
**Descripción:** Convierte archivos de audio a texto usando OpenAI Whisper  
**Alias de:** `Convert-SpeechToText`

**Parámetros:**
- `-AudioFile` - Archivo de audio (obligatorio)
- `-Model` - Modelo Whisper (por defecto: whisper-1)
- `-Language` - Código de idioma (ej: 'es', 'en')
- `-OutputFile` - Guardar transcripción en archivo
- `-OpenInNotepad` - Abrir resultado en Notepad++
- `-CopyToClipboard` - Copiar al portapapeles
- `-Verbose` - Información detallada

**Ejemplos:**
```powershell
# Transcripción básica
S2T "reunión.mp3"

# Con opciones avanzadas
S2T "audio.wav" -Language "es" -OutputFile "transcripcion.txt" -OpenInNotepad -Verbose

# Copiar al portapapeles
S2T "nota_voz.m4a" -CopyToClipboard
```

**Formatos soportados:** mp3, mp4, mpeg, mpga, m4a, wav, webm  
**Límite de tamaño:** 25MB máximo

### `s2thelp`
**Descripción:** Muestra ayuda completa del sistema de transcripción  
**Alias de:** `Show-S2THelp`

**Requisitos:**
- Variable de entorno `OPENAI_API_KEY` configurada
- curl instalado (incluido en Windows 10+)

---

## 🛠️ Herramientas

### `np [archivo]`
**Descripción:** Abre Notepad++ con o sin archivo específico  
**Alias de:** `Open-NotepadPlusPlus`  
**Uso:**
- `np` - Abre Notepad++ vacío
- `np "archivo.txt"` - Abre archivo específico

---

## 📍 Ubicación del Perfil

Todas estas funciones están definidas en:
```
C:\Users\arome\OneDrive\OLD\Documentos\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

## 🔧 Configuración Requerida

### Variables de Entorno
Para el funcionamiento completo, configura:

```powershell
# Para email
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "tu-app-password"

# Para transcripción (establecer manualmente)
$env:OPENAI_API_KEY = "tu-api-key-de-openai"
```

## 💡 Consejos de Uso

1. **Gestión de notas:** Usa `xx` para revisar tareas pendientes, `xxx` para consolidarlas
2. **Email rápido:** Configura credenciales una vez y usa `mail` para envíos rápidos
3. **Transcripción:** Ideal para convertir reuniones grabadas o notas de voz
4. **Navegación:** `g` es perfecto para abrir repos desde terminal
5. **Edición:** `np` + `x` para edición rápida de pendientes

---

*Este documento se actualiza automáticamente cuando se modifican las funciones del perfil*

# 🚀 Comandos y Alias del Perfil PowerShell

## 📋 Índice
- [Navegación y Repositorios](#navegación-y-repositorios)
- [Editores y Archivos](#editores-y-archivos)
- [Gestión de Notas](#gestión-de-notas)
- [Correo Electrónico](#correo-electrónico)
- [Referencia Rápida](#referencia-rápida)

---

## 🗂️ Navegación y Repositorios

### `g`
**Función:** Abrir repositorio Git en Microsoft Edge

**Descripción:** Detecta automáticamente la URL del repositorio Git actual y la abre en el navegador.

**Uso:**
```powershell
g
```

**Funcionalidad:**
- ✅ Obtiene la URL remota del repositorio Git
- ✅ Convierte URLs SSH a HTTPS automáticamente
- ✅ Abre directamente en Microsoft Edge
- ⚠️ Requiere estar en un directorio con repositorio Git

**Ejemplo:**
```powershell
# Estando en un repositorio Git
g
# Resultado: Abre https://github.com/usuario/repo en Edge
```

---

### `notes`
**Función:** Navegar al directorio de notas

**Descripción:** Cambia rápidamente al directorio principal de notas del proyecto.

**Uso:**
```powershell
notes
```

**Ruta destino:**
```
G:\Mi unidad\METANO-IA.ORG\code\Notes
```

---

## 📝 Editores y Archivos

### `readme`
**Función:** Abrir README.md en Notepad++

**Descripción:** Abre rápidamente el archivo README.md del directorio actual en Notepad++.

**Uso:**
```powershell
readme
```

**Requisitos:**
- ✅ Notepad++ instalado en `C:\Program Files\Notepad++\notepad++.exe`
- ✅ Archivo `README.md` en el directorio actual

---

### `np` (alias)
**Función:** Abrir Notepad++ 

**Descripción:** Alias para abrir Notepad++ con o sin archivo específico.

**Uso:**
```powershell
# Abrir Notepad++ vacío
np

# Abrir archivo específico
np archivo.txt
np "ruta/al/archivo.md"
```

**Parámetros:**
- `FileName` (Opcional): Ruta del archivo a abrir

**Ejemplos:**
```powershell
np config.json
np "C:\Users\usuario\documento.txt"
```

---

## 📋 Gestión de Notas

### `xx`
**Función:** Buscar notas en archivos Markdown

**Descripción:** Busca y muestra todas las líneas que empiecen por "XX " o "xx " en archivos .md del directorio actual.

**Uso:**
```powershell
xx
```

**Funcionalidad:**
- 🔍 Busca en todos los archivos `.md` del directorio actual
- 📊 Muestra estadísticas completas de la búsqueda
- 🎯 Busca específicamente líneas que empiecen con "XX " o "xx " seguido de espacio
- 📝 Extrae solo el texto posterior al prefijo

**Salida de ejemplo:**
```
Archivo: proyecto.md
  Línea 15: Revisar documentación de la API
  Línea 23: Implementar validación de datos

========================================
RESUMEN
========================================
Archivos analizados: 5
Archivos con notas: 2
Total de notas: 8
```

---

### `xxx`
**Función:** Extraer y mover notas a archivo de pendientes

**Descripción:** Extrae líneas que empiecen con un patrón específico, las mueve a un archivo de pendientes y las elimina de los archivos originales.

**Uso:**
```powershell
# Uso básico (busca "XX " y guarda en pendientes.md)
xxx

# Uso con patrón personalizado
xxx "TODO " "tareas.md"

# Uso con archivo de salida personalizado
xxx "XX " "mis_pendientes.md"
```

**Parámetros:**
- `SearchPattern` (Opcional): Patrón a buscar (por defecto: "XX ")
- `OutputFile` (Opcional): Archivo de destino (por defecto: "pendientes.md")

**Funcionalidad:**
- ✂️ **MUEVE** las notas (las elimina del archivo original)
- 📁 Procesa todos los archivos `.md` excepto el archivo de destino
- 📊 Muestra estadísticas de procesamiento
- 🎯 Solo extrae texto que tenga contenido después del patrón

**Ejemplos:**
```powershell
# Mover todas las notas "XX " a pendientes.md
xxx

# Mover notas "TODO " a archivo específico
xxx "TODO " "lista_tareas.md"

# Mover notas "FIXME " a archivo de bugs
xxx "FIXME " "bugs_pendientes.md"
```

---

### `x`
**Función:** Abrir archivo de pendientes

**Descripción:** Abre el archivo `pendientes.md` del directorio actual en Notepad++. Si no existe, ofrece crearlo.

**Uso:**
```powershell
x
```

**Funcionalidad:**
- 📂 Busca `pendientes.md` en el directorio actual
- ✅ Si existe: lo abre en Notepad++
- ❓ Si no existe: pregunta si deseas crearlo
- 📝 Si aceptas crear: crea el archivo con estructura básica

**Estructura del archivo creado:**
```markdown
# Pendientes


```

---

## 📧 Correo Electrónico

### `mail` (alias)
**Función:** Envío rápido de correos electrónicos

**Descripción:** Alias para enviar correos de forma rápida usando Gmail SMTP.

**Uso:**
```powershell
mail -To "destino@email.com" -Subject "Asunto" -Body "Mensaje"
```

**Parámetros:**
- `To` (Obligatorio): Dirección de correo de destino
- `Subject` (Obligatorio): Asunto del correo
- `Body` (Obligatorio): Contenido del mensaje
- `Attachments` (Opcional): Array de archivos adjuntos

**Ejemplos:**
```powershell
# Correo simple
mail -To "colega@empresa.com" -Subject "Reunión" -Body "¿Podemos reunirnos mañana?"

# Correo con archivos adjuntos
mail -To "cliente@empresa.com" -Subject "Propuesta" -Body "Adjunto la propuesta" -Attachments @("propuesta.pdf", "presupuesto.xlsx")
```

---

### `Send-GmailMessage`
**Función:** Envío completo de correos con opciones avanzadas

**Descripción:** Función completa para envío de correos con todas las opciones disponibles.

**Uso:**
```powershell
Send-GmailMessage -To "destino@email.com" -Subject "Asunto" -Body "Mensaje" [opciones]
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

**Ejemplos:**
```powershell
# Correo con HTML
Send-GmailMessage -To "newsletter@empresa.com" -Subject "Boletín" -Body "<h1>Noticias</h1><p>Contenido del boletín</p>" -BodyAsHTML

# Correo desde dirección específica
Send-GmailMessage -To "cliente@empresa.com" -From "ventas@miempresa.com" -Subject "Propuesta" -Body "Mensaje"
```

---

### `Set-GmailCredentials`
**Función:** Configurar credenciales de Gmail

**Descripción:** Configura y guarda las credenciales de Gmail para uso automático en envío de correos.

**Uso:**
```powershell
Set-GmailCredentials -Email "tu@gmail.com" -AppPassword "xxxx xxxx xxxx xxxx"
```

**Parámetros:**
- `Email` (Obligatorio): Dirección de Gmail
- `AppPassword` (Obligatorio): Contraseña de aplicación de Gmail

**Funcionalidad:**
- 🔐 Guarda credenciales como variables de entorno del usuario
- 🔄 Las credenciales persisten entre sesiones
- ⚙️ Configuración requerida solo una vez
- 🛡️ Usa contraseñas de aplicación (más seguro)

**Requisitos previos:**
1. ✅ Verificación en 2 pasos habilitada en Gmail
2. ✅ Contraseña de aplicación generada en: https://myaccount.google.com/apppasswords

**Ejemplo:**
```powershell
Set-GmailCredentials -Email "aromero@metano-ia.org" -AppPassword "abcd efgh ijkl mnop"
```

---

### `emailhelp` (alias)
**Función:** Mostrar ayuda de correo electrónico

**Descripción:** Muestra documentación completa y ejemplos de uso de las funciones de correo.

**Uso:**
```powershell
emailhelp
```

**Información mostrada:**
- 📚 Guía paso a paso para configurar credenciales
- 💡 Ejemplos de uso de todos los comandos de correo
- ⚠️ Notas importantes y requisitos
- 🔗 Enlaces a recursos de Gmail

---

## 🚀 Referencia Rápida

### 📁 **Navegación**
| Comando | Función | Uso |
|---------|---------|-----|
| `g` | Abrir repo Git en Edge | `g` |
| `notes` | Ir a directorio Notes | `notes` |

### 📝 **Editores**
| Comando | Función | Uso |
|---------|---------|-----|
| `readme` | Abrir README.md | `readme` |
| `np` | Abrir Notepad++ | `np [archivo]` |

### 📋 **Gestión de Notas**
| Comando | Función | Uso |
|---------|---------|-----|
| `xx` | Buscar notas | `xx` |
| `xxx` | Extraer/mover notas | `xxx [patrón] [archivo]` |
| `x` | Abrir pendientes.md | `x` |

### 📧 **Correo Electrónico**
| Comando | Función | Uso |
|---------|---------|-----|
| `mail` | Envío rápido | `mail -To email -Subject asunto -Body mensaje` |
| `Send-GmailMessage` | Envío completo | `Send-GmailMessage [parámetros]` |
| `Set-GmailCredentials` | Configurar credenciales | `Set-GmailCredentials -Email email -AppPassword pass` |
| `emailhelp` | Ayuda de correo | `emailhelp` |

---

## 🔧 Configuración y Requisitos

### **Software requerido:**
- ✅ PowerShell 5.1 o superior
- ✅ Notepad++ instalado en `C:\Program Files\Notepad++\notepad++.exe`
- ✅ Microsoft Edge (para comando `g`)
- ✅ Git (para comando `g`)

### **Para funciones de correo:**
- ✅ Cuenta de Gmail con verificación en 2 pasos
- ✅ Contraseña de aplicación generada
- ✅ Conexión a internet

### **Ubicación del perfil:**
```
C:\Users\arome\OneDrive\OLD\Documentos\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

---

## 💡 Tips y Trucos

### **Flujo de trabajo con notas:**
1. Usa `xx` para revisar notas existentes
2. Usa `xxx` para mover notas a pendientes
3. Usa `x` para abrir y gestionar pendientes

### **Flujo de trabajo con correo:**
1. Configura credenciales una vez con `Set-GmailCredentials`
2. Usa `mail` para envíos rápidos
3. Usa `Send-GmailMessage` para opciones avanzadas
4. Usa `emailhelp` si necesitas recordar sintaxis

### **Atajos útiles:**
```powershell
# Ir a notas y buscar pendientes
notes; xx

# Procesar notas y abrir pendientes
xxx; x

# Envío rápido de archivo actual por correo
mail -To "destino@email.com" -Subject "Archivo" -Body "Adjunto archivo" -Attachments @((Get-Location).Path + "\archivo.txt")
```

---

**Documento creado:** $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")  
**Perfil PowerShell:** Microsoft.PowerShell_profile.ps1  
**Total de comandos:** 11 funciones + 4 alias  
**Versión:** 1.0

