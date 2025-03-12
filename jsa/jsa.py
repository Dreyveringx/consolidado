import pandas as pd

# Cargar el archivo de Excel
file_path = "consolidado.xlsx"

#Cargar todas las hojas disponibles en el archivo
xls = pd.ExcelFile(file_path)
hojas_disponibles = xls.sheet_names  # Lista de hojas reales en el archivo

#Leer la hoja "CONSOLIDADO"
df = pd.read_excel(file_path, sheet_name="CONSOLIDADO")

#Filtrar filas donde la columna F contenga "JSA"
filas_jsa = df[df.iloc[:, 5].astype(str).str.contains("JSA", case=False, na=False)]
print(filas_jsa)

#Extraer y limpiar los nombres de hojas desde la columna J
hojas_referenciadas = filas_jsa.iloc[:, 9].dropna().unique()
hojas_limpias = [hoja.split("!")[0].strip().replace("'", "").upper() for hoja in hojas_referenciadas]

#Crear un diccionario para almacenar los datos de cada hoja y sus referencias
datos_hojas = {}

#Leer solo las hojas que realmente existen
for hoja in hojas_limpias:
    #Obtener el valor de la columna A donde se hace referencia a la hoja
    referencia_A = filas_jsa.loc[filas_jsa.iloc[:, 9].astype(str).str.upper() == hoja, filas_jsa.columns[0]].values

    if hoja in hojas_disponibles:
        try:
            df_hoja = pd.read_excel(file_path, sheet_name=hoja)
            datos_hojas[hoja] = {"datos": df_hoja, "referencia_A": referencia_A}
        except Exception as e:
            print(f"⚠ Error al leer la hoja {hoja} (Referencia en columna A: {referencia_A}): {e}")
    else:
        print(f"❌ Hoja no encontrada: {hoja} (Referencia en columna A: {referencia_A})")

#Mostrar los datos extraídos(valores de las columnas) de cada hoja junto con la referencia correcta
for hoja, info in datos_hojas.items():
    print(f"\n📄 Datos de la hoja: {hoja} (Referencia en columna A: {info['referencia_A']})")
    print(info["datos"].columns)

