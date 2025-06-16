# Find XX Notes - Script para buscar notas marcadas con XX
# Uso: .\find-xx-notes.ps1 [directorio]
# Si no se especifica directorio, usa el actual

param(
    [string]$Directory = (Get-Location).Path,
    [string]$Pattern = "XX"
)

Write-Host "🔍 Buscando notas marcadas con '$Pattern' en archivos .md..." -ForegroundColor Cyan
Write-Host "📁 Directorio: $Directory" -ForegroundColor Gray
Write-Host ""

# Buscar todos los archivos .md
$mdFiles = Get-ChildItem -Path $Directory -Filter "*.md" -Recurse

if ($mdFiles.Count -eq 0) {
    Write-Host "❌ No se encontraron archivos .md en el directorio especificado" -ForegroundColor Red
    exit 1
}

Write-Host "📄 Archivos .md encontrados: $($mdFiles.Count)" -ForegroundColor Green

# Contadores
$totalNotes = 0
$filesWithNotes = 0

# Buscar líneas con XX en cada archivo
foreach ($file in $mdFiles) {
    $matchingLines = Select-String -Path $file.FullName -Pattern $Pattern -AllMatches
    
    if ($matchingLines) {
        $filesWithNotes++
        
        Write-Host ""
        Write-Host "📁 $($file.Name)" -ForegroundColor Yellow
        Write-Host "   Ruta: $($file.FullName)" -ForegroundColor DarkGray
        
        foreach ($match in $matchingLines) {
            $totalNotes++
            $lineNumber = $match.LineNumber
            $content = $match.Line.Trim()
            
            Write-Host "   📝 Línea $lineNumber`: " -ForegroundColor White -NoNewline
            
            # Resaltar XX en el contenido
            $highlightedContent = $content -replace $Pattern, "[$Pattern]"
            Write-Host $highlightedContent -ForegroundColor Cyan
        }
    }
}

# Resumen final
Write-Host ""
Write-Host "═══════════════════════════════════════" -ForegroundColor DarkGray
Write-Host "📊 RESUMEN DE LA BÚSQUEDA" -ForegroundColor Green
Write-Host "═══════════════════════════════════════" -ForegroundColor DarkGray
Write-Host "📄 Archivos .md analizados: $($mdFiles.Count)" -ForegroundColor White
Write-Host "📁 Archivos con notas: $filesWithNotes" -ForegroundColor White
Write-Host "📝 Total de notas encontradas: $totalNotes" -ForegroundColor White
Write-Host "🔍 Patrón buscado: '$Pattern'" -ForegroundColor White
Write-Host "📍 Directorio: $Directory" -ForegroundColor DarkGray

if ($totalNotes -eq 0) {
    Write-Host ""
    Write-Host "ℹ️  No se encontraron notas con el patrón '$Pattern'" -ForegroundColor Yellow
} else {
    Write-Host ""
    Write-Host "✅ Búsqueda completada exitosamente" -ForegroundColor Green
}

# Opcional: Abrir el archivo con más notas
if ($filesWithNotes -gt 0) {
    Write-Host ""
    $response = Read-Host "¿Deseas abrir el primer archivo con notas? (s/n)"
    if ($response -eq 's' -or $response -eq 'S' -or $response -eq 'y' -or $response -eq 'Y') {
        $firstFileWithNotes = $mdFiles | Where-Object { 
            (Select-String -Path $_.FullName -Pattern $Pattern -Quiet) 
        } | Select-Object -First 1
        
        if ($firstFileWithNotes) {
            Write-Host "🚀 Abriendo $($firstFileWithNotes.Name)..." -ForegroundColor Green
            Start-Process notepad $firstFileWithNotes.FullName
        }
    }
}

