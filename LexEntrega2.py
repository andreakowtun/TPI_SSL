import ply.lex as lex

# Lista de tokens
tokens = (
    'A_STRING', 'LISTA_EQUIPOS', 'LISTA_PROYECTOS', 'LISTA_INTEGRANTES', 'EQUIPO', 
    'DIRECCION', 'INTEGRANTE', 'PROYECTO', 'ESTADO', 'PROTOCOLO', 'CARGO', 'PUERTO', 
    'RUTA', 'DOMINIO', 'SUBDOMINIO', 'VERSION', 'FIRMA_DIGITAL', 'NOMBRE_EQUIPO', 
    'LINK', 'EXTENSION', 'EDAD', 'FOTO', 'EMAIL', 'HABILIDADES', 'SALARIO', 'ACTIVO', 
    'TAREAS', 'TAREA', 'FECHA_INICIO', 'FECHA_FIN', 'VIDEO', 'LLAVE_ABRE', 'LLAVE_CIERRA', 'CORCHETE_ABRE', 'CORCHETE_CIERRA', 'DOS_PUNTOS', 'COMA', 'NUMBER', 'TRUE', 'FALSE', 'NULL'
)

t_LLAVE_ABRE = r'\{'
t_LLAVE_CIERRA = r'\}'
t_CORCHETE_ABRE = r'\['
t_CORCHETE_CIERRA = r'\]'
t_DOS_PUNTOS = r':'
t_COMA = r','


# Definiciones de tokens usando expresiones regulares

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_NULL(t):
    r'null'
    return t

def t_LISTA_EQUIPOS(t):
    r'EQUIPO(\s*,\s*EQUIPO)*'
    return t

def t_VERSION(t):
    r'"versión"\s*:\s* A_STRING,'
    return t

def t_A_STRING(t):
    r'"[^"\n]*"'  # cualquier cosa entre comillas dobles, excepto salto de línea o comillas internas
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
    r'"salario"\s*:\s*\d+\.\d+'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
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

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

ruta = "C:\\Users\\andre\\Desktop\\TPI_SSL\\PruebaCorrecta.json"

#Función para leer JSON manualmente sin `json`
try:
    with open(ruta, "r", encoding="utf-8") as f:
        texto_json = f.read()
        lexer.input(texto_json)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Cargar el archivo sin usar `json`
#texto_json = cargar_json_manual(ruta)

# Alimento el lexer con el contenido extraído
lexer.input(texto_json)

#contador de tokens generados
token_count = 0
# Procesamiento de tokens generados
while True:
    tok = lexer.token()
    if not tok:
        break
    print('')
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
    token_count += 1  # Incrementar contador de tokens procesados



# Mensaje final
if token_count > 0:
    print("\n¡Procesamiento exitoso! Se generaron", token_count, "tokens.")
else:
    print("\nError: No se generaron tokens. Verifica el formato del JSON.")
