# Calculadora-RISCO

RC_Calculadora es un Lenguaje de Dominio Específico (DSL) para realizar operaciones matemáticas, implementado con ANTLR4 y Python. Sigue un estilo funcional con variables inmutables (val) y mutables (var), y respeta la precedencia de operadores.

## Características

- Variables inmutables (`val`) y mutables (`var`)
- Operaciones aritméticas básicas (+, -, *, /, %, ^)
- Comparaciones (==, !=, >, <, >=, <=)
- Operadores lógicos (&&, ||, !)
- Funciones built-in (print, length, sum, sqrt, map, filter, reduce)
- Pipelines con operador `|>`

## Requisitos previos 
Con instrucciones para instalar en
#### Linux (Debian)
- Python 3.8 o superior<br>
`
sudo apt update`<br>
`sudo apt upgrade
`
- Java Runtime (para ANTLR)<br>
`
sudo apt install default-jre
`
## Instalacion

### 1. Ubicarse en la carpeta
`Calculadora-RISCO`

### 2. Crear y activar entorno virtual
`python3 -m venv venv`<br>
`source venv/bin/activate`

### 3. Instalar dependencias
`pip install antlr4-python3-runtime==4.13.2`

### 4. Generar el parser
`chmod +x generar.sh`<br>
`./generar.sh`


 ## ¿Cómo usar RC_Calculadora?
 ### Modo interactivo:
`python src/rc_calculadora.py`
 ### Ejecutar un archivo:
 - Crea un archivo con extensión .rc<br>
`python src/rc_calculadora.py Carpeta/nombre_del_archivo.rc`
 ###
