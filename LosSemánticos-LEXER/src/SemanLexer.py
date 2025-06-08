import ply.lex as lex
import tkinter as tk
import string
import math
from tkinter import filedialog
from PIL import Image, ImageTk

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

# Crear ventana con Tkinter

ventana = tk.Tk()  #VENTANA PRINCIPAL
ventana.title("Lexer - Los Semánticos")
ventana.geometry("1280x650+30+20")
ventana.configure(bg="oldlace")
ventana.iconbitmap("semanticoslogov2.ico")

imagenfondo = Image.open("fondolexer.jpg")
fondo = ImageTk.PhotoImage(imagenfondo)

labelfondo = tk.Label(ventana, image=fondo)  #LABEL FONDO
labelfondo.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(ventana,text="Seleccionar JSON")  #BOTON SELECCIONAR ARCHIVO
button.config(fg="black",bg="lightblue",font=("Arial",12))
button.pack(side="top", padx=10, pady=50)

label1 = tk.LabelFrame(ventana, text="Contenido JSON", bg="white", labelanchor="n") #LABEL CONTENIDO JSON
label1.configure(width=600, height=570)
label1.pack(side="left", padx=10)

analisislabel2 = tk.LabelFrame(ventana, text="Análisis Léxico", bg="white", labelanchor="n")  #LABEL ANALISIS LEXICO
analisislabel2.configure(width=600, height=570)
analisislabel2.pack(side="right", padx=10)

textojson = tk.Text(label1, wrap='word')
textojson.pack(expand=True, fill='both')

analisislex = tk.Text(analisislabel2, wrap='word')
analisislex.pack(expand=True, fill='both')


def seleccionarjson():
    ruta = tk.filedialog.askopenfilename(filetypes=[('Archivos JSON', '*.json'), ('Todos los archivos','*.*')])
    if ruta:
        with open(ruta, 'r') as file_obj:
            contenido = file_obj.read()
            textojson.delete(1.0, tk.END)
            textojson.insert(tk.INSERT, contenido)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            texto_json = f.read()
            lexer.input(texto_json)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit()

    # Alimento el lexer con el contenido extraído
    lexer.input(texto_json)

    # contador de tokens generados
    token_count = 0

    # Procesamiento de tokens generados
    file = open("LexAnalysis.txt", "w")
    while True:
        tok = lexer.token()
        if not tok:
            break
        print('')
        print(tok.type, tok.value, tok.lineno, tok.lexpos)
        file.write(tok.type), file.write(" ") #ESCRIBO EN TXT EXTERNO
        file.write(tok.value), file.write(" ")
        file.write(str(tok.lineno)), file.write(" ")
        file.write(str(tok.lexpos)), file.write(" \n")

        analisislex.insert(tk.INSERT, tok.type), analisislex.insert(tk.INSERT, " ")  #ESCRIBO EN LABEL DE LEXER
        analisislex.insert(tk.INSERT, tok.value), analisislex.insert(tk.INSERT, " ")
        analisislex.insert(tk.INSERT, tok.lineno), analisislex.insert(tk.INSERT, " ")
        analisislex.insert(tk.INSERT, tok.lexpos), analisislex.insert(tk.INSERT, " \n")
        token_count += 1  # Incrementar contador de tokens procesados

    if token_count > 0:
        file.write("\n¡Procesamiento exitoso! Se generaron "), file.write(str(token_count)), file.write(" tokens.")
        analisislex.insert(tk.INSERT, "¡Procesamiento exitoso! Se generaron "), analisislex.insert(tk.INSERT, str(token_count)), analisislex.insert(tk.INSERT, " tokens.")
    else:
        file.write("\nError: No se generaron tokens. Verifica el formato del JSON.")
    # Mensaje final
    if token_count > 0:
        print("\n¡Procesamiento exitoso! Se generaron", token_count, "tokens.")
    else:
        print("\nError: No se generaron tokens. Verifica el formato del JSON.")
    file.close()


button.config(command=seleccionarjson)

ventana.mainloop()

