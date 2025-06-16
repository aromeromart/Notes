# XX Notes Finder
param([string]$Pattern = "XX")

Write-Host "Buscando notas '$Pattern' en archivos .md..." -ForegroundColor Cyan
Write-Host ""

$mdFiles = Get-ChildItem -Filter "*.md"

if ($mdFiles.Count -eq 0) {
    Write-Host "No se encontraron archivos .md" -ForegroundColor Red
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
Write-Host "Archivos analizados: $($mdFiles.Count)" -ForegroundColor White
Write-Host "Archivos con notas: $filesWithNotes" -ForegroundColor White
Write-Host "Total de notas: $totalNotes" -ForegroundColor White

if ($totalNotes -eq 0) {
    Write-Host "No se encontraron notas con '$Pattern'" -ForegroundColor Yellow
}

