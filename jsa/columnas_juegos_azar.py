import pandas as pd
from jsa import datos_hojas  # Importamos las hojas extraídas

# Definir la categoría de "Juegos de suerte" (Juegos de Azar)
hojas_juegos_suerte = [
    "INFORME MENSUAL BETPLAY", "VENTAS BETPLAY", "JUEGO NO LIQUIDADO", 
    "MILOTO", "ASTRO VENTA", "PREMIOS UIAF", "PREMIOS RASPA TODO"
]

#Diccionario para contar cuántas veces aparece cada columna
conteo_columnas = {}

#Recorrer solo las hojas de "Juegos de Azar" y contar las columnas
for hoja in hojas_juegos_suerte:
    if hoja in datos_hojas:
        df = datos_hojas[hoja]["datos"]  # Obtener los datos de la hoja
        
        # 📌 Eliminar columnas completamente vacías
        df = df.dropna(axis=1, how='all')

        # 📌 Contar la frecuencia de cada columna
        for col in df.columns:
            conteo_columnas[col] = conteo_columnas.get(col, 0) + 1  # Sumar 1 cada vez que aparece

#Filtrar solo las columnas que aparecen en UNA SOLA hoja
columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

#Filtrar y eliminar las columnas "Unnamed"
columnas_unicas = [col for col in columnas_unicas if not col.startswith("Unnamed")]

#Convertir en diccionario
diccionario_columnas_unicas = {"Columnas Únicas en Juegos de Azar": columnas_unicas}

# Imprimir el diccionario de columnas exclusivas de "Juegos de Azar"
print("\n📊 Columnas que aparecen SOLO en una hoja de 'Juegos de Azar' (sin 'Unnamed'):")
print(diccionario_columnas_unicas)

"""# Guardar la lista en un archivo Excel (opcional)
df_columnas = pd.DataFrame(diccionario_columnas_unicas)
df_columnas.to_excel("columnas_exclusivas_juegos_azar.xlsx", index=False)
print("\n✅ Archivo 'columnas_exclusivas_juegos_azar.xlsx' generado con éxito.")"""
