# from  import datos_hojas  # Importamos las hojas extraídas

# # Diccionario para contar cuántas veces aparece cada columna
# conteo_columnas = {}

# # Recorrer todas las hojas y contar las columnas
# for info in datos_hojas.values():
#     for col in info["datos"].columns:
#         conteo_columnas[col] = conteo_columnas.get(col, 0) + 1  # Sumar 1 cada vez que aparece

# # Filtrar solo las columnas que aparecen **una sola vez**
# columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

# #Convertir en diccionario
# diccionario_columnas_unicas = {"Columnas Únicas": columnas_unicas}

# #Imprimir el diccionario de columnas exclusivas
# print("\n📊 Columnas que aparecen SOLO en una hoja (sin repetirse en otras):")
# print(diccionario_columnas_unicas)

# """#Guardar la lista en un archivo Excel
# df_columnas = pd.DataFrame(diccionario_columnas_unicas)
# df_columnas.to_excel("columnas_exclusivas.xlsx", index=False)
# print("\nArchivo 'columnas_exclusivas.xlsx' generado con éxito.")"""

import pandas as pd

# Cargar el archivo de Excel
file_path = "consolidado.xlsx"

# Cargar todas las hojas disponibles en el archivo
xls = pd.ExcelFile(file_path)
hojas_disponibles = xls.sheet_names  # Lista de hojas reales en el archivo

# Leer la hoja "CONSOLIDADO"
df = pd.read_excel(file_path, sheet_name="CONSOLIDADO")

# Filtrar filas donde las columnas B (1) o E (4) contengan "Recaudos"
filas_recaudos = df[
    df.iloc[:, [1, 4]]  # Seleccionar solo las columnas B y E
    .astype(str)  # Convertir a string para evitar errores
    .apply(lambda x: x.str.contains("Recaudos", case=False, na=False), axis=1)  # Buscar palabra clave
    .any(axis=1)  # Filtrar filas donde al menos una columna tenga la palabra
]

print(filas_recaudos)

# Extraer y limpiar los nombres de hojas desde la columna J (índice 9)
hojas_referenciadas = filas_recaudos.iloc[:, 9].dropna().unique()
hojas_limpias = [hoja.split("!")[0].strip().replace("'", "").upper() for hoja in hojas_referenciadas]

# Crear un diccionario para almacenar los datos de cada hoja y sus referencias
datos_hojas = {}

# Leer solo las hojas que realmente existen
for hoja in hojas_limpias:
    # Obtener el valor de la columna A donde se hace referencia a la hoja
    referencia_A = filas_recaudos.loc[filas_recaudos.iloc[:, 9].astype(str).str.upper() == hoja, filas_recaudos.columns[0]].values

    if hoja in hojas_disponibles:
        try:
            df_hoja = pd.read_excel(file_path, sheet_name=hoja)
            datos_hojas[hoja] = {"datos": df_hoja, "referencia_A": referencia_A}
        except Exception as e:
            print(f"⚠ Error al leer la hoja {hoja} (Referencia en columna A: {referencia_A}): {e}")
    else:
        print(f"❌ Hoja no encontrada: {hoja} (Referencia en columna A: {referencia_A})")

# Mostrar los datos extraídos de cada hoja junto con la referencia correcta
for hoja, info in datos_hojas.items():
    print(f"\n📄 Datos de la hoja: {hoja} (Referencia en columna A: {info['referencia_A']})")
    print(info["datos"].columns)
