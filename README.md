﻿


# Notes

## Descripción
fichero que explica como voy desarrollando el proyecto Notes

## Configuración Inicial de Git

Comandos utilizados para inicializar el repositorio:

```bash
echo "# Notes" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/aromeromart/Notes.git
git push -u origin main
```

## Comandos Útiles


Tu perfil ahora incluye estas funciones disponibles:
•  g - Abrir repositorio git en el navegador
•  readme - Abrir README.md en Notepad++
•  notes - Cambiar al directorio de notas
•  np - Abrir Notepad++ (alias para Open-NotepadPlusPlus)
•  s y search - Buscar notas en archivos .md (alias para Search-Notes)
•  X para abrir el fichero de pendientes 
•  XX para buscar las tareas pendientes 
•  xxx para mover los pendientes




He creado un backup de tu perfil original en $PROFILE.backup por si necesitas recuperar algo.


## Objetivo

El objetivo del proyecto es crear una arquitectura para introducir notas y que estas sean revisadas por nuestro asistente



# SPRINT 
El acceso a Hyperion será multicanal y habrá cntrol de acceso 
por ahora es simplemente a través de telegram, 
el sistema ha de aprender de si mismo 
ha de guardar lo ue le entra y lo que el va respondiendo 

## code messagetype 
Me contesta tras determinar por código el messageType, hasta 16 casos 
es interesante porque es una funcion prácticamente determinística hecha en python 
lo curioso es que ha sido propuesta por una IA, nos ha ahorrado mucho trabajo 

## RAMA 1 nos devuelve los resultado de messagetype 

## RAMA 2 BASIC LLM CHAIN
que reciba TODO lo que nos da el extractor de informacion, no solo es un generador de message type, tiene un TODO 
todo que se consigue con {{ JSON.stringify($json, null, 2) }}

Se convertiría en un agente especialista en TELEGRAM pero usamos 
realmente no es agente, es una cadena, no lo veo muy oportuno pero ya hace funciones no deterministicas no programadas 

tenemos un articulo que habla de las ventajas del llm chain, parece que hay varios niveles de complejidad 

### multimensaje
A veces llegan varios tipos de mensaje a la vez 
por ejemplo si adjunto un fichero tambien puedo adjuntar un comentarios de texto
es un problema a estudiar, ver como lo tratamos, porque lo he visto 


# WARP y otras notas 
usando wrap para aplicar inteligencia artificial y para construir n8n, aquí doy un salto en la academia 
voy a empezar a trabajar para la academia 

quizá no necesite un MPC Server para Telegram, y me tenga que centrar en la verticalidad delo que quiero 
x quizá debiera definir la verticalidad o hacer algo muy vertical, p.ej. ante audio transcipción

el colmo es que hiciera peticiones y que las fueramos desarrollando por detrás 

# dilema agente vs deterministico
Lo interesante sería que fuera agente al principio y que dependiendo de las demandas del usuario entonces se modificar el comportamiento, 
esto supone hacer destilación 

puedo hacer cosas deterministicas que un agente falla a manudo, pero indefectiveblemente un agente será capaz de hacerlo 
aunque yo lo habre afianzado con una herramienta probablemente ya no sea necesario 

 
arquitectura en principio de agentes, la más rápida, el codigo deterministico vs el agente, el gran dilema, en el que siempre irá ganando el agente, pero lo que quiero es que aprenda aprenda
y si tiro por esta linea han de ser agetnes, o agentes que aprendan de codigo que yo les pase
o que puedan cambiar su propio código 
y a esto apunta n8n 


# nodo de seguridad 
y claramente determinístico 

## pero el problema es el SET, me pierdo con los sets 
un set de todo desde el prinipio 
aquí me hago un lio, preguntar 
por sobre todo como me refiero a las variables en python 
eto es lo dificultoso

# EL GRAN PROBLEMA DE LA ARQUITECTURA , del front-end , un dashboard 
Si no presentamos un buen front-end la cosa no funciona 
y hay de distintos tipos, web y para movil, son los dos front-end o interfaces principales,
un front-end que sea un dashboard, que incluso fuera dinámico, cambiado por el usuario, le haríamos actualizaciones 


# TELEGRAM ERRORES Y TELGRAM LOG 
Desde luego tengo los errores pero es fundamental el log (





## bots de Telegram @BotFaher
puede ser un sitio donde albergar cosas 
estamos con wrap simulando casi vibe coding 



