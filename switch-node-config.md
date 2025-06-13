# Configuración Switch Node - Todos los Tipos de Mensaje

## Arquitectura del Switch

```
Message Type Detector → Switch Node (16 salidas)
                        ├── 0: text
                        ├── 1: photo
                        ├── 2: video
                        ├── 3: voice
                        ├── 4: audio
                        ├── 5: document
                        ├── 6: sticker
                        ├── 7: animation
                        ├── 8: location
                        ├── 9: contact
                        ├── 10: venue
                        ├── 11: poll
                        ├── 12: dice
                        ├── 13: game
                        ├── 14: video_note
                        └── 15: unknown/default
```

## Configuración JSON del Switch Node

```json
{
  "name": "Message Type Router",
  "type": "n8n-nodes-base.switch",
  "parameters": {
    "mode": "expression",
    "output": "specified",
    "outputsCount": 16,
    "rules": {
      "rules": [
        {
          "output": 0,
          "expression": "={{ $json.messageType === 'text' }}"
        },
        {
          "output": 1,
          "expression": "={{ $json.messageType === 'photo' }}"
        },
        {
          "output": 2,
          "expression": "={{ $json.messageType === 'video' }}"
        },
        {
          "output": 3,
          "expression": "={{ $json.messageType === 'voice' }}"
        },
        {
          "output": 4,
          "expression": "={{ $json.messageType === 'audio' }}"
        },
        {
          "output": 5,
          "expression": "={{ $json.messageType === 'document' }}"
        },
        {
          "output": 6,
          "expression": "={{ $json.messageType === 'sticker' }}"
        },
        {
          "output": 7,
          "expression": "={{ $json.messageType === 'animation' }}"
        },
        {
          "output": 8,
          "expression": "={{ $json.messageType === 'location' }}"
        },
        {
          "output": 9,
          "expression": "={{ $json.messageType === 'contact' }}"
        },
        {
          "output": 10,
          "expression": "={{ $json.messageType === 'venue' }}"
        },
        {
          "output": 11,
          "expression": "={{ $json.messageType === 'poll' }}"
        },
        {
          "output": 12,
          "expression": "={{ $json.messageType === 'dice' }}"
        },
        {
          "output": 13,
          "expression": "={{ $json.messageType === 'game' }}"
        },
        {
          "output": 14,
          "expression": "={{ $json.messageType === 'video_note' }}"
        }
      ],
      "fallbackOutput": 15
    }
  }
}
```

## Configuración Manual en n8n

### Paso 1: Crear Switch Node
1. Añadir nodo **Switch**
2. Configurar **Mode**: `Expression`
3. Configurar **Output**: `Specified Amount`
4. **Number of Outputs**: `16`

### Paso 2: Configurar cada condición

| Salida | Tipo | Expresión | Descripción |
|--------|------|-----------|-------------|
| **0** | `text` | `{{ $json.messageType === 'text' }}` | Mensajes de texto |
| **1** | `photo` | `{{ $json.messageType === 'photo' }}` | Imágenes/fotos |
| **2** | `video` | `{{ $json.messageType === 'video' }}` | Videos |
| **3** | `voice` | `{{ $json.messageType === 'voice' }}` | Mensajes de voz |
| **4** | `audio` | `{{ $json.messageType === 'audio' }}` | Archivos de audio |
| **5** | `document` | `{{ $json.messageType === 'document' }}` | Documentos (PDF, DOC, etc.) |
| **6** | `sticker` | `{{ $json.messageType === 'sticker' }}` | Stickers/pegatinas |
| **7** | `animation` | `{{ $json.messageType === 'animation' }}` | GIFs animados |
| **8** | `location` | `{{ $json.messageType === 'location' }}` | Ubicación geográfica |
| **9** | `contact` | `{{ $json.messageType === 'contact' }}` | Información de contacto |
| **10** | `venue` | `{{ $json.messageType === 'venue' }}` | Lugares específicos |
| **11** | `poll` | `{{ $json.messageType === 'poll' }}` | Encuestas |
| **12** | `dice` | `{{ $json.messageType === 'dice' }}` | Dados animados |
| **13** | `game` | `{{ $json.messageType === 'game' }}` | Juegos |
| **14** | `video_note` | `{{ $json.messageType === 'video_note' }}` | Videos circulares |
| **15** | `unknown` | **Default/Fallback** | Tipos no reconocidos |

## Configuración por Prioridad

### 🔴 Alta Prioridad (Implementar primero)
**Salidas 0-5**: Conectar a procesadores específicos
- **0 (text)** → Procesador de texto con IA
- **1 (photo)** → Procesador de imágenes
- **2 (video)** → Procesador de videos  
- **3 (voice)** → Transcriptor de voz
- **4 (audio)** → Procesador de audio
- **5 (document)** → Analizador de documentos

### 🟡 Media Prioridad (Fase 2)
**Salidas 6-10**: Respuestas básicas
- **6-10** → Nodo "Respuesta Estándar" que diga "Tipo recibido: [tipo]"

### 🟢 Baja Prioridad (Futuro)
**Salidas 11-14**: Funcionalidades especiales
- **11-14** → Nodo "En desarrollo" 

### ⚪ Fallback
**Salida 15**: Manejo de errores
- **15 (unknown)** → Nodo "Tipo no soportado"

## Flujo Completo Sugerido

```
Telegram Trigger
    ↓
Message Type Detector
    ↓
Switch Node (16 salidas)
    ├── 0 (text) → AI Text Processor → Telegram Response
    ├── 1 (photo) → Image Analyzer → Telegram Response
    ├── 2 (video) → Video Handler → Telegram Response
    ├── 3 (voice) → Voice Transcriber → AI Text Processor
    ├── 4 (audio) → Audio Handler → Telegram Response
    ├── 5 (document) → Document Analyzer → Telegram Response
    ├── 6-10 → Basic Response: "Recibido: [tipo]"
    ├── 11-14 → "Funcionalidad en desarrollo"
    └── 15 (unknown) → "Tipo de mensaje no soportado"
```

## Testing del Switch

### Test Cases por Salida
1. **Texto**: "Hola" → Salida 0
2. **Foto**: Enviar imagen → Salida 1
3. **Video**: Enviar video → Salida 2
4. **Voz**: Grabar audio → Salida 3
5. **Audio**: Archivo MP3 → Salida 4
6. **Documento**: PDF → Salida 5
7. **Sticker**: Enviar sticker → Salida 6
8. **GIF**: Enviar GIF → Salida 7
9. **Ubicación**: Compartir ubicación → Salida 8
10. **Contacto**: Compartir contacto → Salida 9
11. **Lugar**: Enviar lugar → Salida 10
12. **Encuesta**: Crear poll → Salida 11
13. **Dado**: Enviar dado → Salida 12
14. **Juego**: Enviar juego → Salida 13
15. **Video Note**: Video circular → Salida 14
16. **Desconocido**: Cualquier otro → Salida 15

## Ejemplo de Implementación Gradual

### Fase 1: Solo 6 salidas activas
```
├── 0 (text) → AI Processor
├── 1 (photo) → "Imagen recibida"
├── 2-4 → "Multimedia recibido"
├── 5 (document) → "Documento recibido"
└── 15 (default) → "Tipo no soportado aún"
```

### Fase 2: Expandir a todas las salidas
Activar procesadores específicos para cada tipo según necesidad.

## Ventajas de Tener Todas las Salidas

✅ **Preparado para el futuro**: Todas las salidas listas
✅ **Fácil expansión**: Solo conectar nuevos procesadores
✅ **Debug claro**: Sabes exactamente qué tipo llegó
✅ **Escalabilidad**: Cada tipo tiene su flujo independiente
✅ **Mantenimiento**: Fácil habilitar/deshabilitar tipos

---

**Configuración recomendada**: Crear las 16 salidas desde el inicio, pero conectar procesadores gradualmente según prioridad.

