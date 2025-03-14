import pandas as pd

#Cargar el archivo de Excel
file_path = "consolidado.xlsx"

#Cargar todas las hojas disponibles en el archivo
xls = pd.ExcelFile(file_path)
hojas_disponibles = xls.sheet_names  # Lista de hojas reales en el archivo

#Leer la hoja "CONSOLIDADO"
df = pd.read_excel(file_path, sheet_name="CONSOLIDADO")

#Filtrar filas donde las columnas B (índice 1) o E (índice 4) contengan "Caja" o "Corresponsal"
filas_escrutinio = df[
    df.iloc[:, 1].astype(str).str.contains("Caja|Corresponsal", case=False, na=False) |
    df.iloc[:, 4].astype(str).str.contains("Caja|Corresponsal", case=False, na=False)
]

print(filas_escrutinio)

#Extraer y limpiar los nombres de hojas desde la columna J (índice 9 en Python)
hojas_referenciadas = filas_escrutinio.iloc[:, 9].dropna().unique()
hojas_limpias = [hoja.split("!")[0].strip().replace("'", "").upper() for hoja in hojas_referenciadas]

#Crear un diccionario para almacenar los datos de cada hoja y sus referencias
datos_hojas = {}

#Leer solo las hojas que realmente existen
for hoja in hojas_limpias:
    #Obtener el valor de la columna A donde se hace referencia a la hoja
    referencia_A = filas_escrutinio.loc[filas_escrutinio.iloc[:, 9].astype(str).str.upper() == hoja, filas_escrutinio.columns[0]].values

    if hoja in hojas_disponibles:
        try:
            df_hoja = pd.read_excel(file_path, sheet_name=hoja)
            #Extraer solo las columnas que necesitas (ejemplo: A, B y C)
            datos_hojas[hoja] = {"datos": df_hoja, "referencia_A": referencia_A}  # Guardar datos y referencia
        except Exception as e:
            print(f"⚠ Error al leer la hoja {hoja} (Referencia en columna A: {referencia_A}): {e}")
    else:
        print(f"❌ Hoja no encontrada: {hoja} (Referencia en columna A: {referencia_A})")

#Mostrar los datos extraídos de cada hoja junto con la referencia correcta
for hoja, info in datos_hojas.items():
    print(f"\n📄 Datos de la hoja: {hoja} (Referencia en columna A: {info['referencia_A']})")
    print(info["datos"].columns)
