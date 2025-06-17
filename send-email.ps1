# Funcion para enviar correos electronicos usando Gmail
function Send-GmailMessage {
    param(
        [Parameter(Mandatory=$true)]
        [string]$To,
        
        [Parameter(Mandatory=$true)]
        [string]$Subject,
        
        [Parameter(Mandatory=$true)]
        [string]$Body,
        
        [Parameter(Mandatory=$false)]
        [string[]]$Attachments = @(),
        
        [Parameter(Mandatory=$false)]
        [string]$From,
        
        [Parameter(Mandatory=$false)]
        [string]$SmtpServer = "smtp.gmail.com",
        
        [Parameter(Mandatory=$false)]
        [int]$Port = 587,
        
        [Parameter(Mandatory=$false)]
        [switch]$BodyAsHTML = $false
    )
    
    try {
        # Configurar credenciales desde variables de entorno o solicitar
        if (-not $From) {
            $From = $env:GMAIL_USER
            if (-not $From) {
                $From = Read-Host "Ingresa tu direccion de Gmail"
            }
        }
        
        $Password = $env:GMAIL_APP_PASSWORD
        if (-not $Password) {
            $SecurePassword = Read-Host "Ingresa tu contrasena de aplicacion de Gmail" -AsSecureString
            $Password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($SecurePassword))
        }
        
        # Crear objeto de credenciales
        $SecurePass = ConvertTo-SecureString $Password -AsPlainText -Force
        $Credential = New-Object System.Management.Automation.PSCredential($From, $SecurePass)
        
        # Configurar parametros del correo
        $MailParams = @{
            SmtpServer = $SmtpServer
            Port = $Port
            UseSsl = $true
            Credential = $Credential
            From = $From
            To = $To
            Subject = $Subject
            Body = $Body
            Encoding = 'UTF8'
        }
        
        # Agregar attachments si existen
        if ($Attachments.Count -gt 0) {
            $ValidAttachments = @()
            foreach ($attachment in $Attachments) {
                if (Test-Path $attachment) {
                    $ValidAttachments += $attachment
                } else {
                    Write-Warning "Archivo no encontrado: $attachment"
                }
            }
            if ($ValidAttachments.Count -gt 0) {
                $MailParams.Attachments = $ValidAttachments
            }
        }
        
        # Configurar si el cuerpo es HTML
        if ($BodyAsHTML) {
            $MailParams.BodyAsHtml = $true
        }
        
        # Enviar el correo
        Send-MailMessage @MailParams
        Write-Host "Correo enviado exitosamente a $To" -ForegroundColor Green
        
    } catch {
        Write-Error "Error enviando correo: $($_.Exception.Message)"
        
        # Sugerencias de solucion segun el tipo de error
        if ($_.Exception.Message -match "authentication") {
            Write-Host "Sugerencia: Verifica que estes usando una contrasena de aplicacion, no tu contrasena normal de Gmail." -ForegroundColor Yellow
            Write-Host "Puedes generar una aqui: https://myaccount.google.com/apppasswords" -ForegroundColor Yellow
        }
        
        if ($_.Exception.Message -match "SSL") {
            Write-Host "Sugerencia: Problema con SSL. Verifica tu conexion a internet." -ForegroundColor Yellow
        }
    }
}

# Funcion simplificada con alias 'mail'
function Send-QuickMail {
    param(
        [Parameter(Mandatory=$true)]
        [string]$To,
        
        [Parameter(Mandatory=$true)]
        [string]$Subject,
        
        [Parameter(Mandatory=$true)]
        [string]$Body,
        
        [Parameter(Mandatory=$false)]
        [string[]]$Attachments = @()
    )
    
    Send-GmailMessage -To $To -Subject $Subject -Body $Body -Attachments $Attachments
}

Set-Alias -Name mail -Value Send-QuickMail -Force

# Funcion para configurar credenciales como variables de entorno
function Set-GmailCredentials {
    param(
        [Parameter(Mandatory=$true)]
        [string]$Email,
        
        [Parameter(Mandatory=$true)]
        [string]$AppPassword
    )
    
    [Environment]::SetEnvironmentVariable("GMAIL_USER", $Email, "User")
    [Environment]::SetEnvironmentVariable("GMAIL_APP_PASSWORD", $AppPassword, "User")
    
    # Tambien establecer para la sesion actual
    $env:GMAIL_USER = $Email
    $env:GMAIL_APP_PASSWORD = $AppPassword
    
    Write-Host "Credenciales de Gmail configuradas exitosamente" -ForegroundColor Green
    Write-Host "Email: $Email" -ForegroundColor Cyan
    Write-Host "Las credenciales se han guardado como variables de entorno del usuario" -ForegroundColor Yellow
}

# Funcion para mostrar ayuda
function Show-EmailHelp {
    Write-Host "FUNCIONES DE CORREO ELECTRONICO" -ForegroundColor Cyan
    Write-Host "================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. Configurar credenciales (solo una vez):" -ForegroundColor Yellow
    Write-Host "   Set-GmailCredentials -Email 'tu@gmail.com' -AppPassword 'tu-contrasena-app'"
    Write-Host ""
    Write-Host "2. Enviar correo simple:" -ForegroundColor Yellow
    Write-Host "   mail -To 'destino@email.com' -Subject 'Asunto' -Body 'Mensaje'"
    Write-Host ""
    Write-Host "3. Enviar con archivos adjuntos:" -ForegroundColor Yellow
    Write-Host "   mail -To 'destino@email.com' -Subject 'Asunto' -Body 'Mensaje' -Attachments @('archivo1.txt', 'archivo2.pdf')"
    Write-Host ""
    Write-Host "4. Enviar correo completo:" -ForegroundColor Yellow
    Write-Host "   Send-GmailMessage -To 'destino@email.com' -Subject 'Asunto' -Body 'Mensaje' -BodyAsHTML"
    Write-Host ""
    Write-Host "NOTAS IMPORTANTES:" -ForegroundColor Red
    Write-Host "- Necesitas generar una contrasena de aplicacion en: https://myaccount.google.com/apppasswords"
    Write-Host "- NO uses tu contrasena normal de Gmail"
    Write-Host "- Asegurate de tener habilitada la verificacion en 2 pasos en Gmail"
}

Set-Alias -Name emailhelp -Value Show-EmailHelp -Force

Write-Host "Funciones de correo cargadas. Usa 'emailhelp' para ver la ayuda completa." -ForegroundColor Green

