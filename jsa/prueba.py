import pandas as pd
from jsa import datos_hojas  # Importamos las hojas extraídas

# Diccionario para almacenar solo las filas que cumplen con "Juegos de Azar"
datos_jsa = {}

#Filtrar filas que contengan "JSA" en alguna columna
for hoja, info in datos_hojas.items():
    df = info["datos"]

    #Verificar si alguna columna contiene "JSA"
    df_jsa = df[df.astype(str).apply(lambda x: x.str.contains("JSA", case=False, na=False)).any(axis=1)]

    # Si hay coincidencias, guardarlas
    if not df_jsa.empty:
        datos_jsa[hoja] = df_jsa

#Guardar los resultados en un archivo Excel
with pd.ExcelWriter("reporte_jsa.xlsx") as writer:
    for hoja, df in datos_jsa.items():
        df.to_excel(writer, sheet_name=hoja, index=False)

print("\n✅ Archivo 'reporte_jsa.xlsx' generado con éxito, con solo las filas que contienen 'JSA'.")
