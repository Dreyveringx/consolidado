from Filtrar_hojas import datos_hojas  # Importamos las hojas extraídas

# Diccionario para contar cuántas veces aparece cada columna
conteo_columnas = {}

# Recorrer todas las hojas y contar las columnas
for info in datos_hojas.values():
    for col in info["datos"].columns:
        conteo_columnas[col] = conteo_columnas.get(col, 0) + 1  # Sumar 1 cada vez que aparece

# Filtrar solo las columnas que aparecen **una sola vez**
columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

#Convertir en diccionario
diccionario_columnas_unicas = {"Columnas Únicas": columnas_unicas}

#Imprimir el diccionario de columnas exclusivas
print("\n📊 Columnas que aparecen SOLO en una hoja (sin repetirse en otras):")
print(diccionario_columnas_unicas)

# Guardar la lista en un archivo TXT
with open("columnas_exclusivas.txt", "w", encoding="utf-8") as file:
    file.write("📊 Columnas que aparecen SOLO en una hoja (sin repetirse en otras):\n")
    for columna in columnas_unicas:
        file.write(f"{columna}\n")

print("\nArchivo 'columnas_escrutinio.txt' generado con éxito.")

"""#Guardar la lista en un archivo Excel
df_columnas = pd.DataFrame(diccionario_columnas_unicas)
df_columnas.to_excel("columnas_exclusivas.xlsx", index=False)
print("\nArchivo 'columnas_exclusivas.xlsx' generado con éxito.")"""