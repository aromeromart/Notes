# Función para buscar notas en archivos .md
# Agregar esta función al final de tu perfil de PowerShell ($PROFILE)

function Search-Notes {
    param([string]$Pattern = "XX")
    
    Write-Host "Buscando notas '$Pattern' en archivos .md..." -ForegroundColor Cyan
    Write-Host ""
    
    $currentDir = Get-Location
    $mdFiles = Get-ChildItem -Filter "*.md"
    
    if ($mdFiles.Count -eq 0) {
        Write-Host "No se encontraron archivos .md en $currentDir" -ForegroundColor Red
        return
    }
    
    Write-Host "Archivos .md encontrados: $($mdFiles.Count)" -ForegroundColor Green
    Write-Host ""
    
    $totalNotes = 0
    $filesWithNotes = 0
    
    foreach ($file in $mdFiles) {
        $matches = Select-String -Path $file.FullName -Pattern $Pattern
        
        if ($matches) {
            $filesWithNotes++
            Write-Host "Archivo: $($file.Name)" -ForegroundColor Yellow
            
            foreach ($match in $matches) {
                $totalNotes++
                Write-Host "  Linea $($match.LineNumber): $($match.Line.Trim())" -ForegroundColor Cyan
            }
            Write-Host ""
        }
    }
    
    Write-Host "========================================" -ForegroundColor DarkGray
    Write-Host "RESUMEN" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor DarkGray
    Write-Host "Directorio: $currentDir" -ForegroundColor DarkGray
    Write-Host "Archivos analizados: $($mdFiles.Count)" -ForegroundColor White
    Write-Host "Archivos con notas: $filesWithNotes" -ForegroundColor White
    Write-Host "Total de notas: $totalNotes" -ForegroundColor White
    
    if ($totalNotes -eq 0) {
        Write-Host "No se encontraron notas con '$Pattern'" -ForegroundColor Yellow
    }
}

# Crear alias 's' para la función
Set-Alias -Name s -Value Search-Notes

# Crear alias 'search' para la función
Set-Alias -Name search -Value Search-Notes

# Mensaje de confirmación
Write-Host "✅ Función Search-Notes cargada con alias 's' y 'search'" -ForegroundColor Green

