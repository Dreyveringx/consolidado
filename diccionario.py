import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter
import string

# Descargar stopwords si es la primera vez
nltk.download('stopwords')

# Cargar el archivo Excel
ruta_excel = "consolidado.xlsx"  # Cambia esto por la ruta real
df = pd.read_excel(ruta_excel)  # 🔹 Aquí se carga correctamente el archivo

# Seleccionar las columnas de texto
columnas_texto = ["Ruta", "Reporte Solicitado"]  # 🔹 Asegúrate de que estos nombres sean correctos en tu Excel
df_textos = df[columnas_texto].dropna().astype(str)  # 🔹 Filtrar columnas y eliminar nulos

# Preprocesamiento: convertir a minúsculas, eliminar puntuación
stop_words = set(stopwords.words('spanish'))  # 🔹 Lista de stopwords en español
palabras_totales = []

for index, fila in df_textos.iterrows():
    texto_completo = " ".join(fila)  # 🔹 Unir el contenido de ambas columnas en un solo texto
    palabras = texto_completo.lower().translate(str.maketrans('', '', string.punctuation)).split()
    palabras = [p for p in palabras if p not in stop_words and len(p) > 2]  # 🔹 Filtrar palabras vacías y cortas
    palabras_totales.extend(palabras)

# Contar frecuencia de palabras
frecuencia = Counter(palabras_totales)

# Obtener las palabras clave más comunes
palabras_clave = dict(frecuencia.most_common(60))  # 🔹 Ajusta la cantidad según necesites

# Guardar en un archivo TXT
ruta_txt = "diccionario_palabras_clave.txt"
with open(ruta_txt, "w", encoding="utf-8") as f:
    for palabra, freq in palabras_clave.items():
        f.write(f"{palabra}: {freq}\n")

print(f"Diccionario de palabras clave guardado en '{ruta_txt}'")
