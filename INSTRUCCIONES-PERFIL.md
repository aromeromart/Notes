
## Pasos para configurar la función en tu perfil:

### 1. Ubicar tu perfil de PowerShell

Ejecuta este comando para ver dónde está tu perfil:
```powershell
$PROFILE
```

### 2. Crear o editar el perfil

Si el archivo no existe, créalo:
```powershell
New-Item -Path $PROFILE -Type File -Force
```

### 3. Añadir la función al perfil

Abre el archivo de perfil en el editor:
```powershell
notepad $PROFILE
```

O con tu editor preferido:
```powershell
code $PROFILE  # Si tienes VS Code
```

### 4. Copiar la función

Añade el contenido completo del archivo `extract-todos.ps1` al final de tu perfil.

O mejor aún, añade esta línea que carga la función desde el archivo:
```powershell
. "G:\Mi unidad\METANO-IA.ORG\code\Notes\extract-todos.ps1"
```

### 5. Recargar el perfil

Para aplicar los cambios sin reiniciar PowerShell:
```powershell
. $PROFILE
```

## Uso de la función

### Comando básico:
```powershell
```

### Comandos con parámetros:
```powershell
# Buscar un patrón diferente

# Guardar en un archivo diferente

# Ambos parámetros
```

## Lo que hace la función:

1. **Busca** en todos los archivos `.md` del directorio actual y subdirectorios
2. **Encuentra** líneas que contienen el patrón (por defecto "
3. **Extrae** el patrón y todo el texto que viene después
4. **Añade** los elementos extraídos a `pendiente.md` con timestamp
5. **Borra** el patrón y el texto que le sigue de los archivos originales
6. **Mantiene** el resto del contenido intacto

## Ejemplos de uso:

### Antes:
```markdown
# Mi documento
- Tarea importante
- Enviar email
- Revisar código
```


**Archivo original:**
```markdown
# Mi documento
- Tarea importante
- Enviar email
- Revisar código
```

**pendiente.md:**
```markdown
# Pendientes

## Elementos extraidos - 2025-06-16 20:20:23

-
-
```

## Características avanzadas:

- ✅ **Recursivo**: Busca en subdirectorios
- ✅ **Timestamp**: Cada extracción tiene fecha y hora
- ✅ **Origen**: Indica de qué archivo viene cada elemento
- ✅ **Seguro**: No modifica archivos sin el patrón
- ✅ **Flexible**: Patrón y archivo de salida configurables
- ✅ **Limpio**: Elimina líneas que quedan vacías

## Solución de problemas:

### Error: "No se reconoce como cmdlet"
La función no se cargó correctamente. Verifica:
1. Que el archivo `extract-todos.ps1` existe
2. Que la ruta en el perfil es correcta
3. Que recargaste el perfil con `. $PROFILE`

### Error de permisos
Si PowerShell no permite ejecutar scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### La función no encuentra archivos
Verifica que estás en un directorio que contiene archivos `.md`

---


