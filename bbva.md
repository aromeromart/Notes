# Proyecto BBVA - Sistema de Cotizaciones en Tiempo Real

*Creado el 16 de junio de 2025*

## 🏦 Descripción del Proyecto

Sistema completo para monitorear las cotizaciones del Banco Bilbao Vizcaya Argentaria (BBVA) desde PowerShell en tiempo real, integrado con sistemas de notificación y análisis.

---

## 🎯 Objetivos del Proyecto

### **Principales:**
- ✅ Obtener cotización de BBVA en tiempo real
- ✅ Monitoreo continuo con alertas
- ✅ Integración con notificaciones (Telegram)
- ✅ Comparativa con otros bancos españoles
- ✅ Historial de datos en CSV

### **Secundarios:**
- 📊 Análisis de tendencias
- 🤖 Automatización de decisiones
- 📱 Notificaciones inteligentes
- 💾 Almacenamiento de datos históricos

---

## 🚀 Funciones Implementadas

### **📊 Cotización Básica: `bbva`**
```powershell
# Uso básico
bbva

# Con información detallada
bbva -Detailed

# Con alerta de precio
bbva -Alert -AlertPrice 8.50

# Guardar datos en CSV
bbva -SaveToFile
```

**Características:**
- 💰 Precio actual en tiempo real
- 📈 Cambio y porcentaje vs. cierre anterior
- 📊 Volumen de transacciones
- 🏢 Capitalización de mercado
- 🎯 Rangos diarios y anuales (modo detallado)
- 🎨 Colores según ganancia/pérdida

### **👁️ Monitoreo Continuo: `bbva-watch`**
```powershell
# Monitoreo básico (5 minutos)
bbva-watch

# Monitoreo personalizado
bbva-watch -IntervalSeconds 15 -Duration 600

# Con alerta de precio
bbva-watch -AlertPrice 8.50 -Duration 1800
```

**Características:**
- ⏰ Actualización automática configurable
- 🚨 Alertas de precio en tiempo real
- 📱 Notificaciones por Telegram automáticas
- ⏹️ Control manual (Ctrl+C para detener)
- 📊 Información visual actualizada

### **🏦 Comparativa de Bancos: `bbva-compare`**
```powershell
bbva-compare
```

**Bancos incluidos:**
- 🟦 BBVA (BBVA.MC)
- 🔴 Santander (SAN.MC)
- 🟣 CaixaBank (CABK.MC)
- 🟡 Sabadell (SAB.MC)

### **❓ Ayuda del Sistema: `bbvahelp`**
```powershell
bbvahelp
```

---

## 🔧 Configuración y Requisitos

### **Requisitos del Sistema:**
- ✅ PowerShell 5.1 o superior
- ✅ Conexión a internet
- ✅ Windows 10+ (para curl nativo)
- ✅ API de Yahoo Finance (gratuita)

### **Integración Opcional:**
- 📱 **Telegram**: Para notificaciones automáticas
- 📧 **Email**: Para reportes periódicos
- 💾 **CSV**: Para análisis histórico

### **No requiere:**
- ❌ API Keys de pago
- ❌ Registro en servicios financieros
- ❌ Software adicional

---

## 📈 Ejemplos de Uso Prácticos

### **🔍 Consulta Rápida**
```powershell
# Ver precio actual
bbva

# Resultado:
# 🏦 BANCO BILBAO VIZCAYA ARGENTARIA (BBVA)
# ═══════════════════════════════════════
# 💰 Precio actual: 8.345 EUR
# ⬆️ Cambio: +0.125 EUR (+1.52%)
# 📈 Cierre anterior: 8.220 EUR
# 📊 Volumen: 15,234,567 acciones
```

### **📊 Análisis Detallado**
```powershell
bbva -Detailed

# Información adicional:
# 📋 INFORMACIÓN DETALLADA
# ─────────────────────────
# 📊 Rango día: 8.200 - 8.380 EUR
# 📅 Rango 52 sem: 6.850 - 9.120 EUR
# 🎯 Símbolo: BBVA.MC
# 🏛️ Mercado: Bolsa de Madrid (BME)
```

### **🚨 Sistema de Alertas**
```powershell
# Configurar alerta
bbva -Alert -AlertPrice 8.50

# Si BBVA llega a 8.50 EUR:
# 🚨 ALERTA: BBVA ha alcanzado 8.50 EUR
# + Notificación automática por Telegram
```

### **📱 Monitoreo para Trading**
```powershell
# Monitoreo intensivo (actualización cada 10 segundos)
bbva-watch -IntervalSeconds 10 -Duration 3600 -AlertPrice 8.45

# Perfecto para:
# - Seguimiento de sesión bursátil
# - Decisiones de trading
# - Análisis de volatilidad
```

### **📊 Comparativa de Sector**
```powershell
bbva-compare

# Resultado:
# 🏦 COMPARACIÓN BANCOS ESPAÑOLES
# ═══════════════════════════════
# BBVA        : 8.345 EUR ⬆️ +0.125 (+1.52%)
# Santander   : 4.234 EUR ⬇️ -0.056 (-1.31%)
# CaixaBank   : 4.567 EUR ⬆️ +0.023 (+0.51%)
# Sabadell    : 1.234 EUR ➡️ +0.000 (+0.00%)
```

### **💾 Registro Histórico**
```powershell
# Guardar datos para análisis
bbva -SaveToFile

# Genera: bbva_cotizaciones.csv
# Formato: fecha,precio,cambio,porcentaje,volumen
# 2025-06-16 23:15:30,8.345,+0.125,+1.52,15234567
```

---

## 🔗 Integración con Otros Sistemas

### **📱 Notificaciones por Telegram**
```powershell
# Configuración automática de alertas
if ($precioActual -ge $precioObjetivo) {
    t "🚨 ALERTA BBVA: Precio actual $precioActual EUR" -Silent
}
```

### **📧 Reportes por Email**
```powershell
# Reporte diario automático
$reporte = bbva -Detailed
mail -To "inversor@empresa.com" -Subject "Reporte BBVA $(Get-Date -Format 'dd/MM/yyyy')" -Body $reporte
```

### **📝 Notas y Seguimiento**
```powershell
# Integración con sistema de notas
"XX Revisar BBVA a las $(Get-Date -Format 'HH:mm') - Precio: $(bbva | Select-Object -ExpandProperty Price)" | Add-Content "trading.md"
```

---

## 📊 Casos de Uso del Proyecto

### **👨‍💼 Inversor Individual**
- ✅ Seguimiento diario de inversiones
- ✅ Alertas de oportunidades de compra/venta
- ✅ Análisis de tendencias
- ✅ Registro histórico personal

### **🏢 Gestión de Carteras**
- ✅ Monitoreo de múltiples posiciones
- ✅ Alertas automáticas para equipos
- ✅ Reportes periódicos
- ✅ Integración con sistemas internos

### **📚 Análisis y Estudio**
- ✅ Recopilación de datos históricos
- ✅ Comparativas de sector bancario
- ✅ Estudios de volatilidad
- ✅ Backtesting de estrategias

### **🤖 Trading Automatizado**
- ✅ Señales de entrada/salida
- ✅ Monitoreo 24/7 (en horario bursátil)
- ✅ Integración con APIs de brokers
- ✅ Gestión de riesgo automatizada

---

## 🔮 Roadmap y Mejoras Futuras

### **🎯 Versión 2.0 (Planificada)**
- 📊 **Gráficos en terminal** usando ASCII
- 🔄 **Múltiples símbolos** (IBEX 35 completo)
- 📈 **Indicadores técnicos** (RSI, MACD, etc.)
- 🎯 **Órdenes automáticas** (stop-loss, take-profit)

### **🎯 Versión 3.0 (Conceptual)**
- 🤖 **Machine Learning** para predicciones
- 📱 **Dashboard web** integrado
- 🔗 **APIs de brokers** para trading real
- 📊 **Análisis fundamental** automatizado

---

## 📚 Fuentes de Datos

### **Principal: Yahoo Finance API**
- ✅ **Gratuita** y sin límites básicos
- ✅ **Datos en tiempo real** (con delay mínimo)
- ✅ **Cobertura global** de mercados
- ✅ **Historial extenso** disponible
- ✅ **API estable** y confiable

### **Símbolo Utilizado: BBVA.MC**
- 🎯 BBVA en Bolsa de Madrid
- 💱 Cotización en EUR
- 🕐 Horario: 09:00 - 17:30 CET
- 📊 Datos incluyen: precio, volumen, rangos

---

## 🛡️ Consideraciones Legales y Éticas

### **⚠️ Advertencias:**
- 📊 Los datos tienen delay mínimo (15-20 minutos)
- 💰 **No constituye asesoramiento financiero**
- 📈 Past performance no garantiza resultados futuros
- 🎯 Usar solo para análisis e información

### **✅ Uso Responsable:**
- 📚 Para educación e investigación
- 📊 Análisis técnico personal
- 🔍 Seguimiento de inversiones existentes
- 💡 Desarrollo de conocimiento financiero

---

## 🔧 Troubleshooting

### **❌ Error: "No se pudieron obtener datos"**
```powershell
# Verificar conexión
Test-NetConnection google.com -Port 443

# Verificar Yahoo Finance
Invoke-RestMethod "https://query1.finance.yahoo.com/v8/finance/chart/BBVA.MC"
```

### **❌ Error: "Comando no reconocido"**
```powershell
# Recargar perfil
. $PROFILE

# Verificar función
Get-Command bbva
```

### **🐌 Respuesta lenta**
- 🌐 Verificar conexión a internet
- ⏰ Yahoo Finance puede tener delays
- 🔄 Reintentar en unos minutos

---

## 📞 Soporte y Contribuciones

### **📧 Contacto:**
- Email: aromero@metano-ia.org
- Proyecto: METANO-IA.ORG
- Documentación: Este archivo (bbva.md)

### **🔄 Actualizaciones:**
- El sistema se actualiza automáticamente desde Yahoo Finance
- La documentación se mantiene en este archivo
- Nuevas funciones se agregan al perfil de PowerShell

---

*Documento creado automáticamente el $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")*  
*Proyecto integrado en: Microsoft.PowerShell_profile.ps1*  
*Versión actual: 1.0*  
*Estado: Producción*

