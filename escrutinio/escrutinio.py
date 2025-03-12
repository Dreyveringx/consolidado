import pandas as pd

# Cargar el archivo de Excel
file_path = "consolidado.xlsx"

# Leer la hoja "CONSOLIDADO"
df = pd.read_excel(file_path, sheet_name="CONSOLIDADO")

# Verificar los nombres de las columnas
print(df.columns)

# Filtrar donde la columna 2 y la columna 4 contengan "Escrutinio" (sin importar mayúsculas)
resultado = df[
    df.iloc[:, [1, 4]].apply(lambda x: x.astype(str).str.contains("Escrutinio", case=False, na=False)).any(axis=1)
]

# Mostrar los resultados
print(resultado)
