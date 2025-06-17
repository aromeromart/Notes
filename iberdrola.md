# Proyecto Iberdrola - Sistema de Cotizaciones Energéticas

*Creado el 16 de junio de 2025*

## ⚡ Descripción del Proyecto

Sistema completo para monitorear las cotizaciones de Iberdrola S.A. y el sector energético español desde PowerShell en tiempo real, con análisis sectorial y comparativas de utilities.

---

## 🎯 Objetivos del Proyecto

### **Principales:**
- ✅ Obtener cotización de Iberdrola en tiempo real
- ✅ Monitoreo continuo con alertas específicas
- ✅ Comparativa con otras utilities españolas
- ✅ Análisis del sector energético completo
- ✅ Integración con notificaciones (Telegram)
- ✅ Historial de datos en CSV

### **Sectoriales:**
- 🌍 Análisis de transición energética
- ⚡ Seguimiento de utilities españolas
- 📊 Tendencias del sector renovable
- 🔄 Comparativas de performance sectorial

---

## 🚀 Funciones Implementadas

### **⚡ Cotización Básica: `iberdrola`**
```powershell
# Uso básico
iberdrola

# Con información detallada
iberdrola -Detailed

# Con alerta de precio
iberdrola -Alert -AlertPrice 12.50

# Guardar datos en CSV
iberdrola -SaveToFile
```

**Características específicas de Iberdrola:**
- ⚡ Precio actual en tiempo real
- 🌍 Información del sector energético
- 📊 Volumen de transacciones
- 🏢 Capitalización de mercado
- 🔋 Context específico de utilities
- 🎨 Colores según ganancia/pérdida

### **👁️ Monitoreo Continuo: `iberdrola-watch`**
```powershell
# Monitoreo básico (5 minutos)
iberdrola-watch

# Monitoreo personalizado
iberdrola-watch -IntervalSeconds 15 -Duration 600

# Con alerta de precio para trading energético
iberdrola-watch -AlertPrice 12.50 -Duration 1800
```

**Características del monitoreo:**
- ⏰ Actualización automática configurable
- 🚨 Alertas de precio específicas del sector
- 📱 Notificaciones por Telegram automáticas
- ⏹️ Control manual (Ctrl+C para detener)
- 📊 Información visual actualizada

### **⚡ Comparativa Utilities: `iberdrola-compare`**
```powershell
iberdrola-compare
```

**Utilities españolas incluidas:**
- ⚡ **Iberdrola** (IBE.MC)
- 🔌 **Endesa** (ELE.MC) 
- 🔥 **Naturgy** (NTGY.MC)
- 🗼 **REE** (REE.MC)

### **🌍 Análisis Sectorial: `energy-analysis`**
```powershell
energy-analysis
```

**Incluye:**
- 📊 Resumen del comportamiento sectorial
- 📈 Número de valores en alza/baja
- 📊 Cambio promedio del sector
- 🔄 Volumen total de transacciones
- 💡 Contexto de transición energética

### **❓ Ayuda del Sistema: `iberdrolahelp`**
```powershell
iberdrolahelp
```

---

## 🔧 Configuración y Requisitos

### **Requisitos del Sistema:**
- ✅ PowerShell 5.1 o superior
- ✅ Conexión a internet
- ✅ Windows 10+ (para curl nativo)
- ✅ API de Yahoo Finance (gratuita)

### **Integración Opcional:**
- 📱 **Telegram**: Para alertas del sector energético
- 📧 **Email**: Para reportes sectoriales
- 💾 **CSV**: Para análisis histórico
- 📊 **Análisis cruzado**: Con sistema BBVA

### **No requiere:**
- ❌ API Keys de pago
- ❌ Registro en servicios financieros
- ❌ Software adicional
- ❌ Conocimiento previo del sector

---

## 📈 Ejemplos de Uso Prácticos

### **⚡ Consulta Rápida**
```powershell
# Ver precio actual de Iberdrola
iberdrola

# Resultado:
# ⚡ IBERDROLA S.A. (IBE)
# ═══════════════════════
# 💰 Precio actual: 12.145 EUR
# ⬆️ Cambio: +0.085 EUR (+0.71%)
# 📈 Cierre anterior: 12.060 EUR
# 📊 Volumen: 8,456,789 acciones
```

### **🌍 Análisis Sectorial Completo**
```powershell
iberdrola -Detailed

# Información adicional:
# 📋 INFORMACIÓN DETALLADA
# ─────────────────────────
# 📊 Rango día: 12.050 - 12.180 EUR
# 📅 Rango 52 sem: 9.850 - 13.250 EUR
# 🎯 Símbolo: IBE.MC
# 🏛️ Mercado: Bolsa de Madrid (BME)
# ⚡ Sector: Energético - Utilities
# 🌍 Negocio: Energía Renovable y Distribución
```

### **🚨 Sistema de Alertas Energéticas**
```powershell
# Configurar alerta para oportunidades de inversión
iberdrola -Alert -AlertPrice 12.50

# Si Iberdrola llega a 12.50 EUR:
# 🚨 ALERTA: Iberdrola ha alcanzado 12.50 EUR
# + Notificación automática por Telegram
```

### **📊 Comparativa del Sector Utilities**
```powershell
iberdrola-compare

# Resultado:
# ⚡ COMPARACIÓN UTILITIES ESPAÑOLAS
# ═════════════════════════════════
# ⚡ Iberdrola  : 12.145 EUR ⬆️ +0.085 (+0.71%)
# 🔌 Endesa     : 18.230 EUR ⬇️ -0.125 (-0.68%)
# 🔥 Naturgy    : 24.560 EUR ⬆️ +0.340 (+1.40%)
# 🗼 REE        : 19.875 EUR ➡️ +0.000 (+0.00%)
```

### **🌍 Análisis de Mercado Energético**
```powershell
energy-analysis

# Resultado:
# 🌍 ANÁLISIS DEL SECTOR ENERGÉTICO ESPAÑOL
# ═════════════════════════════════════════
# 
# 📊 RESUMEN DEL SECTOR:
#   📈 Valores en alza: 2
#   📉 Valores en baja: 1
#   📊 Cambio promedio: +0.36%
#   🔄 Volumen total approx: 45.2M acciones
# 
# 💡 CONTEXTO DEL SECTOR:
#   ⚡ Transición energética en curso
#   🌱 Focus en renovables y sostenibilidad
#   📈 Inversión en redes inteligentes
#   🇪🇺 Regulación europea en evolución
```

### **💾 Monitoreo para Trading Energético**
```powershell
# Monitoreo intensivo del sector utilities
iberdrola-watch -IntervalSeconds 15 -Duration 3600 -AlertPrice 12.40

# Perfecto para:
# - Trading de utilities españolas
# - Seguimiento de transición energética
# - Análisis de volatilidad sectorial
# - Decisiones de inversión sostenible
```

### **💾 Registro Histórico Sectorial**
```powershell
# Guardar datos para análisis de tendencias
iberdrola -SaveToFile

# Genera: iberdrola_cotizaciones.csv
# Formato: fecha,precio,cambio,porcentaje,volumen
# 2025-06-16 23:20:45,12.145,+0.085,+0.71,8456789
```

---

## 🔗 Integración con Ecosistema de Trading

### **📱 Alertas Sectoriales por Telegram**
```powershell
# Configuración automática para utilities
if ($precioIberdrola -ge $objetivoSector) {
    t "⚡ ALERTA UTILITIES: Iberdrola $precioIberdrola EUR - Sector en alza" -Silent
}
```

### **📧 Reportes Sectoriales por Email**
```powershell
# Reporte semanal del sector energético
$reporteUtilities = energy-analysis
$datosIberdrola = iberdrola -Detailed
mail -To "inversiones@empresa.com" -Subject "Reporte Semanal Utilities $(Get-Date -Format 'dd/MM/yyyy')" -Body "$reporteUtilities`n`n$datosIberdrola"
```

### **📊 Integración con BBVA (Comparativa Sectorial)**
```powershell
# Comparar performance bancario vs utilities
Write-Host "📊 COMPARATIVA MULTI-SECTORIAL" -ForegroundColor Cyan
bbva-compare
Write-Host ""
iberdrola-compare
Write-Host ""
energy-analysis
```

### **📝 Seguimiento de Cartera Sostenible**
```powershell
# Integración con sistema de notas para ESG
"XX Revisar portfolio ESG - Iberdrola: $(iberdrola | Select-Object -ExpandProperty Price) EUR" | Add-Content "esg_portfolio.md"
```

---

## 📊 Casos de Uso del Proyecto

### **🌍 Inversor ESG/Sostenible**
- ✅ Seguimiento de utilities renovables
- ✅ Análisis de transición energética
- ✅ Comparativas de sostenibilidad
- ✅ Alertas de oportunidades verdes

### **⚡ Trading Sectorial**
- ✅ Monitoreo de utilities españolas
- ✅ Arbitraje entre companies del sector
- ✅ Análisis de volatilidad sectorial
- ✅ Timing de entrada/salida

### **🏢 Gestión de Carteras Energéticas**
- ✅ Diversificación dentro del sector
- ✅ Rebalanceo automático
- ✅ Reportes de performance sectorial
- ✅ Gestión de riesgo regulatorio

### **📚 Análisis de Mercado Energético**
- ✅ Estudios de correlación sectorial
- ✅ Impact de políticas energéticas
- ✅ Tendencias de transición verde
- ✅ Benchmarking europeo

---

## 🔮 Roadmap y Mejoras Futuras

### **🎯 Versión 2.0 (Planificada)**
- 🌍 **Utilities europeas** (EDF, Enel, E.ON)
- 📊 **Indicadores ESG** automatizados
- ⚡ **Precios de energía** en tiempo real
- 🔋 **Capacidad renovable** por company

### **🎯 Versión 3.0 (Visión)**
- 🤖 **AI para predicción** de precios energéticos
- 🌡️ **Factores climáticos** integrados
- 📜 **Análisis regulatorio** automatizado
- 🔄 **Trading automático** de utilities

---

## 🌍 Contexto del Sector Energético

### **⚡ Iberdrola - Perfil de Company**
- 🏢 **Líder mundial** en energías renovables
- 🌍 **Presencia global**: España, Reino Unido, EE.UU., Brasil
- 💰 **Capitalización**: ~70-80B EUR
- 🔋 **Mix energético**: 80%+ renovables
- 📈 **Crecimiento**: Inversión masiva en eólica y solar

### **🇪🇸 Sector Utilities Español**
- ⚡ **Transición acelerada** hacia renovables
- 🏛️ **Regulación europea** pro-sostenibilidad
- 💰 **Inversión récord** en infraestructura verde
- 📊 **Consolidación** del mercado

### **🌍 Tendencias Globales**
- 🌱 **Net Zero** commitments
- 🔋 **Electrificación** de la economía
- 💰 **ESG investing** boom
- ⚡ **Smart grids** deployment

---

## 📚 Fuentes de Datos

### **Principal: Yahoo Finance API**
- ✅ **Datos real-time** de Bolsa de Madrid
- ✅ **Cobertura completa** utilities españolas
- ✅ **Historial extenso** para backtesting
- ✅ **API gratuita** y estable

### **Símbolos Utilizados:**
- ⚡ **IBE.MC** - Iberdrola
- 🔌 **ELE.MC** - Endesa
- 🔥 **NTGY.MC** - Naturgy
- 🗼 **REE.MC** - Red Eléctrica

### **Datos Incluidos:**
- 💰 Precio en tiempo real
- 📊 Volumen de transacciones
- 📈 Rangos diarios y anuales
- 🏢 Capitalización de mercado
- 📅 Histórico completo

---

## 🛡️ Consideraciones del Sector

### **⚠️ Riesgos Específicos:**
- 🏛️ **Riesgo regulatorio** alto
- 🌡️ **Dependencia climática** (renovables)
- 💰 **Intensivo en capital** (CAPEX alto)
- ⚡ **Volatilidad de precios** energéticos

### **✅ Oportunidades:**
- 🌍 **Transición energética** global
- 💰 **Financiación verde** abundante
- 📈 **Crecimiento sostenible** estructural
- 🔋 **Nuevas tecnologías** (storage, H2)

### **📊 Uso Responsable:**
- 📚 Para análisis fundamental de sector
- 🔍 Research de inversión sostenible
- 📊 Seguimiento de portfolio ESG
- 💡 Educación en mercados energéticos

---

## 🔧 Troubleshooting Específico

### **❌ Error: "No datos de utilities"**
```powershell
# Verificar conectividad específica
Test-NetConnection finance.yahoo.com -Port 443

# Probar utility específica
Invoke-RestMethod "https://query1.finance.yahoo.com/v8/finance/chart/IBE.MC"
```

### **⚡ Datos inconsistentes entre utilities**
- 🕐 **Horarios de trading** diferentes
- 📊 **Volúmenes** muy variables por company
- 🔄 **Delays** distintos en data feeds

### **🐌 Performance lenta en análisis sectorial**
- 🌐 Múltiples llamadas API simultáneas
- ⏰ Considerar intervalos más largos
- 📊 Cachear resultados para analysis

---

## 📞 Soporte y Contribuciones

### **📧 Contacto:**
- Email: aromero@metano-ia.org
- Proyecto: METANO-IA.ORG
- Especialización: Mercados energéticos
- Documentación: Este archivo (iberdrola.md)

### **🔄 Actualizaciones Sectoriales:**
- El sistema se adapta a cambios regulatorios
- Nuevas utilities se pueden agregar fácilmente
- Análisis sectorial se expande automáticamente
- Integration con trends ESG

---

## 💡 Tips para Trading de Utilities

### **⚡ Mejores Prácticas:**
1. **Monitorear en horario** 09:00-17:30 CET
2. **Considerar factores** climáticos y regulatorios
3. **Diversificar** entre diferentes utilities
4. **Seguir noticias** de política energética
5. **Análizar correlaciones** con precios de energía

### **📊 Análisis Técnico Específico:**
- **Soporte/Resistencia**: Niveles regulatorios históricos
- **Volumen**: Indicador clave en utilities
- **Estacionalidad**: Patterns de demanda energética
- **Correlaciones**: Con índices ESG y clima

---

*Documento creado automáticamente el $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")*  
*Proyecto integrado en: Microsoft.PowerShell_profile.ps1*  
*Especialización: Sector energético y utilities*  
*Versión actual: 1.0*  
*Estado: Producción*

