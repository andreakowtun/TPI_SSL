from ply import lex
#import json
#import re

#Lista de tokens (simbolos no terminales)
tokens = (
    'A_STRING',
    'LISTA_EQUIPOS',
    'LISTA_PROYECTOS',
    'LISTA_INTEGRANTES',
    'EQUIPO',
    'DIRECCION',
    'INTEGRANTE',
    'PROYECTO',
    'ESTADO',
    'PROTOCOLO',
    'CARGO',
    'PUERTO',
    'RUTA',
    'DOMINIO',
    'SUBDOMINIO',
    'VERSION',
    'FIRMA_DIGITAL',
    'NOMBRE_EQUIPO',
    'LINK',
    'EXTENSION',
    'INTEGRANTE',
    'EDAD',
    'CARGO', 
    'FOTO', 
    'EMAIL', 
    'HABILIDADES', 
    'SALARIO', 
    'ACTIVO',
    'PROYECTO', 
    'ESTADO', 
    'TAREAS', 
    'TAREA',
    'FECHA_INICIO', 
    'FECHA_FIN', 
    'VIDEO',
)

# Expreciones regulares para tokens simples
"""t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'"""

#Funciones para convertir simbolos no terminales en terminales

def t_LISTA_EQUIPOS(t):
    r'EQUIPO(\s*,\s*EQUIPO)*'
    return t

def t_VERSION(t):
    r'"versión"\s*:\s* A_STRING,'
    return t

def t_A_STRING(t):
    r'"[a-zA-Z0-9_-]+"'
    return t

def t_VERSION_NULL(t):
    r'"versión"\s*:\s*null,'
    return t

def t_FIRMA_DIGITAL(t):
    r'"firma_digital"\s*:\s*[a-zA-Z0-9_-]+'
    return t

def t_FIRMA_DIGITAL_NULL(t):
    r'"firma_digital"\s*:\s*null'
    return t

def t_EQUIPO(t):
    r'\{\s*"nombre_equipo"\s*:\s*[a-zA-Z0-9_-]+,\s*"identidad_equipo"\s*:\s*[a-zA-Z0-9:/._-]+,\s*' \
    r'(("direccion"\s*:\s*\{.*?\},\s*)?)' \
    r'(("link"\s*:\s*[a-zA-Z0-9:/._-]+,\s*)?)' \
    r'"carrera"\s*:\s*[a-zA-Z0-9_-]+,\s*"asignatura"\s*:\s*[a-zA-Z0-9_-]+,\s*"universidad_regional"\s*:\s*[a-zA-Z0-9_-]+,\s*' \
    r'"alianza_equipo"\s*:\s*[a-zA-Z0-9_-]+,\s*"integrantes"\s*:\s*\[.*?\],\s*"proyectos"\s*:\s*\[.*?\]\s*\}'
    return t

def t_LINK(t):
    r'λ|null|"[a-zA-Z]+://[a-zA-Z0-9.-]+(:[0-9]+)?(/[a-zA-Z0-9.-]+)*,"'
    return t

def t_PROTOCOLO(t):
    r'"(?:http|https|ftp|ftps)"' #uso ? para que solo reconozca una opcion a la vez
    return t

def t_DIRECCION(t):
    r'"direccion"\s*:\s*\{\s*"calle"\s*:\s*[a-zA-Z0-9_-]+,\s*"ciudad"\s*:\s*[a-zA-Z0-9_-]+,\s*"país"\s*:\s*[a-zA-Z0-9_-]+\s*\},'
    return t

def t_LISTA_INTEGRANTES(t):
    r'INTEGRANTE(\s*,\s*INTEGRANTE)*'
    return t

def t_LISTA_PROYECTOS(t):
    r'PROYECTO(\s*,\s*PROYECTO)*'
    return t

def t_DOMINIO(t):
    r'([a-zA-Z0-9_-]+\.)?[a-zA-Z0-9_-]+\.(?:com|org|net|edu|gov|ar|es|fr)'
    return t

def t_SUBDOMINIO(t):
    r'[a-zA-Z0-9_-]+\.'
    return t

def t_EXTENSION(t):
    r'"(?:com|org|net|edu|gov|ar|es|fr)"'
    return t

def t_PUERTO(t):
    r':\d+'
    return t

def t_RUTA(t):
    r'(/[a-zA-Z0-9_-]+)+'
    return t

def t_INTEGRANTE(t):
    r'"integrante"\s*:\s*"[^"]*"'
    return t

def t_EDAD(t):
    r'"edad"\s*:\s*\d+'
    return t

def t_CARGOS(t):
    r'"Product\sAnalyst"|"Project\sManager"|"UX\sdesigner"|"Marketing"|"Developer"|"Devops"|"DB\sadmin"'
    return t

def t_FOTO(t):
    r'"foto"\s*:\s*"[^"]*"'
    return t

def t_EMAIL(t):
    r'"email"\s*:\s*"[^"]*"'
    return t

def t_HABILIDADES(t):
    r'"habilidades"\s*:\s*\[[^\]]*\]'
    return t

def t_SALARIO(t):
    r'"salario"\s*:\s*\d+(\.\d+)?'
    return t

def t_ACTIVO(t):
    r'"activo"\s*:\s*(true|false)'
    return t

def t_PROYECTO(t):
    r'"proyecto"\s*:\s*"[^"]*"'
    return t

def t_ESTADOS(t):
    r'"To\sdo"|"In\sprogress"|"Canceled"|"Done"|"On\shold"'
    return t

def t_TAREAS(t):
    r'"tareas"\s*:\s*\[[^\]]*\]'
    return t

def t_TAREA(t):
    r'"tarea"\s*:\s*"[^"]*"'
    return t

def t_FECHA_INICIO(t):
    r'"fecha_inicio"\s*:\s*"[^"]*"'
    return t

def t_FECHA_FIN(t):
    r'"fecha_fin"\s*:\s*"[^"]*"'
    return t

def t_VIDEO(t):
    r'"video"\s*:\s*"[^"]*"'
    return t


#################################
# Construccion del lexer
lexer = lex.lex()


# Imprimir tokens generados
for token in lexer:
    print(token)


def t_NUMBER(t):
    r'\d+'
    return t

# Define una regla para que podamos rastrear los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# string que contiene los caracteres ignorados (espacios y tabulaciones)
t_ignore  = ' \t'

# manejo de error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Cargar JSON manualmente como una cadena

def cargar_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()  # Retorna el contenido del archivo
    except Exception:
        print("No abrió :p")
        return ""  # Devuelve una cadena vacía en caso de error
    

json_texto = cargar_json("C:\\Users\\andre\\Desktop\\TPI_SSL\\PruebaCorrecta.json")
lexer.input(json_texto)

#for tok in lexer:
#    print(tok)

#Los tokens devueltos por lexer.token() son instancias de LexToken. 
# Este objeto tiene los atributos tok.type, tok.value, tok.lineno y tok.lexpos. 
# El siguiente código muestra un ejemplo de acceso a estos atributos:

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)

