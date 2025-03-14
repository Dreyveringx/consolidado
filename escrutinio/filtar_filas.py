import pandas as pd

#Ruta del archivo Excel
file_path = "consolidado.xlsx"

#Cargar el archivo de Excel
xls = pd.ExcelFile(file_path)

#Verificar si existe la hoja "CONSOLIDADO"
sheet_name = "CONSOLIDADO" if "CONSOLIDADO" in xls.sheet_names else xls.sheet_names[0]

#Cargar la hoja en un DataFrame
df = pd.read_excel(xls, sheet_name=sheet_name, engine="openpyxl")

#Filtrar filas donde la columna B (índice 1) o E (índice 4) contengan "Escrutinio"
df_filtrado = df[df.iloc[:, [1, 4]].astype(str).apply(lambda x: x.str.contains("Escrutinio", case=False, na=False)).any(axis=1)]

#Contar y mostrar los resultados
print(f"Total de filas encontradas: {df_filtrado.shape[0]}")
print(df_filtrado)

#Guardar el resultado en un nuevo archivo Excel
df_filtrado.to_excel("filtrado_Escrutinio.xlsx", index=False)
print("Archivo 'filtrado_recaudos.xlsx' guardado con los datos filtrados.")
