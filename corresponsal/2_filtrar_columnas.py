import pandas as pd
from filtrar_filas import datos_hojas  # Importamos las hojas extraídas

# Diccionario para contar cuántas veces aparece cada columna
conteo_columnas = {}

# Recorrer todas las hojas y contar las columnas
for info in datos_hojas.values():
    for col in info["datos"].columns:
        conteo_columnas[col] = conteo_columnas.get(col, 0) + 1  # Sumar 1 cada vez que aparece

# Filtrar solo las columnas que aparecen una sola vez
columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

# Guardar la lista en un archivo TXT
with open("columnas_unicas.txt", "w", encoding="utf-8") as file:
    for columna in columnas_unicas:
        file.write(f'"{columna}",\n')

print("\n✅ Archivo 'columnas-unicas.txt' generado con éxito.")
