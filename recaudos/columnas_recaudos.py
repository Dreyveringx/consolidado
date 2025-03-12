import pandas as pd
from columnas_generales import datos_hojas  # Importamos las hojas extraídas desde recaudos.py

# Diccionario para contar cuántas veces aparece cada columna
conteo_columnas = {}

# Recorrer todas las hojas de "Recaudos" y contar las columnas
for info in datos_hojas.values():
    for col in info["datos"].columns:
        conteo_columnas[col] = conteo_columnas.get(col, 0) + 1  # Sumar 1 cada vez que aparece

# Filtrar solo las columnas que aparecen en UNA SOLA hoja
columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

# Filtrar y eliminar las columnas "Unnamed"
columnas_unicas = [col for col in columnas_unicas if not col.startswith("Unnamed")]

# Convertir en diccionario
diccionario_columnas_unicas = {"Columnas Únicas en Recaudos": columnas_unicas}

# Imprimir el diccionario de columnas exclusivas de "Recaudos"
print("\n📊 Columnas que aparecen SOLO en una hoja de 'Recaudos' (sin 'Unnamed'):")
print(diccionario_columnas_unicas)

# Guardar la lista en un archivo de texto
ruta_txt = "columnas_unicas_recaudos.txt"
with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write("📊 Columnas que aparecen SOLO en una hoja de 'Recaudos' (sin 'Unnamed'):\n\n")
    for columna in columnas_unicas:
        f.write(f"- {columna}\n")

print(f"\n✅ Archivo '{ruta_txt}' generado con éxito.")
