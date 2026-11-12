import re
from variables import *

def busqueda_posibles_DEs(texto, mapa):
    texto_minusculas = texto.lower()

    # Creamos una expresión regular (Regex) compilada para máxima velocidad.
    # Ordenamos por longitud descendente para que "etilparabeno sódico" se detecte 
    # antes que "etilparabeno" (evita falsos positivos por solapamiento).
    sinonimos_ordenados = sorted(mapa.keys(), key=len, reverse=True)
    # re.escape protege caracteres como "&" en "fd&c"
    patron_regex = re.compile('|'.join(map(re.escape, sinonimos_ordenados)), re.IGNORECASE)

    # Usamos nuestro "cartel gigante" (patron_regex) para encontrar todas las coincidencias.
    # Esto nos devolverá una lista con las palabras que coincidan. Ej: ['e102', 'tartrazina']
    coincidencias = patron_regex.findall(texto_minusculas)

    posibles_DEs_encontrados = set()

    for coincidencia in coincidencias:
        nombre_principal = mapa[coincidencia]  # Obtenemos el nombre principal del DE
        posibles_DEs_encontrados.add(nombre_principal)  # Añadimos el nombre principal al set
    
    return list(posibles_DEs_encontrados)  # Convertimos el set a lista antes de devolverlo


def combinar_limpiar_posibles_DEs(fila):
    lista_aditivos = fila["posibles_DEs_en_aditivos"]
    lista_ingredientes = fila["posibles_DEs_en_ingredientes"]

    lista_final = set()

    for de in lista_aditivos:
        lista_final.add(de)

    for de in lista_ingredientes:
        lista_final.add(de)

    return list(lista_final)


def combinar_limpiar_posibles_DEs(fila):
    lista_aditivos = fila["posibles_DEs_en_aditivos"]
    lista_ingredientes = fila["posibles_DEs_en_ingredientes"]

    lista_final = set()

    for de in lista_aditivos:
        lista_final.add(de)

    for de in lista_ingredientes:
        lista_final.add(de)

    return list(lista_final)