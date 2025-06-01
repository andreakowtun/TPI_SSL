#The following example shows how lex.py is used to write a simple tokenizer.

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'EQUIPOS',
    'EQUIPO',
    'DIRECCION',
    'INTEGRANTES',
    'INTEGRANTE',
    'PROYECTO',
    'PROYECTOS',
    'TAREAS',
    'TAREA',
    'ESTADO',
    'PROTOCOLO',
    'CARGO',
    'PUERTO',
    'RUTA',
    'DOMINIO',
    'EMAIL',
    'VERSION',
    'FIRMA_DIGITAL',
    'NOMBRE_EQUIPO',
    'LINK',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
#En PLY, las funciones con el prefijo t_ representan reglas léxicas.
# NUMBER indica que esta regla busca identificar tokens que representen números.
# \d+ significa "uno o más dígitos" (0-9).
#Esto permite identificar números enteros como 123, 42, etc.
#Conversión a Entero t.value = int(t.value):
#t.value contiene la cadena encontrada por la expresión regular.
#Se convierte en un entero (int) antes de devolver el token.

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
    r''
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
    r'(/[a-zA-Z0-9_-]+)*'
    return t








def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#To use the lexer, you first need to feed it some input text using its input() method. 
# After that, repeated calls to token() produce tokens. The following code shows how this works:


# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
#When executed, the example will produce the following output:

"""$ python example.py
LexToken(NUMBER,3,2,1)
LexToken(PLUS,'+',2,3)
LexToken(NUMBER,4,2,5)
LexToken(TIMES,'*',2,7)
LexToken(NUMBER,10,2,10)
LexToken(PLUS,'+',3,14)
LexToken(MINUS,'-',3,16)
LexToken(NUMBER,20,3,18)
LexToken(TIMES,'*',3,20)
LexToken(NUMBER,2,3,21)"""

#Lexers also support the iteration protocol. So, you can write the above loop as follows:

for tok in lexer:
    print(tok)
#The tokens returned by lexer.token() are instances of LexToken. This object has attributes tok.type, tok.value, tok.lineno, and tok.lexpos. The following code shows an example of accessing these attributes:

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, tok.value, tok.lineno, tok.lexpos)