import pandas as pd
from filtrar_columnas import datos_hojas  # Importamos las hojas extraídas

# 1️⃣ Contar cuántas veces aparece cada columna
conteo_columnas = {}

for info in datos_hojas.values():
    for col in info["datos"].columns:
        conteo_columnas[col] = conteo_columnas.get(col, 0) + 1

# 2️⃣ Filtrar solo las columnas que aparecen en UNA SOLA hoja
columnas_unicas = [col for col, count in conteo_columnas.items() if count == 1]

# 3️⃣ Convertir todo a string y eliminar "Unnamed"
columnas_unicas = [str(col) for col in columnas_unicas if isinstance(col, str) and not str(col).startswith("Unnamed")]

# 4️⃣ Definir categorías y palabras clave asociadas
categorias = {
    "Identificación del Usuario": ["USUARIO", "CEDULA", "NOMBRES"],
    "Información de la Transacción": ["PIN", "NUMERO_CONTROL", "NUMERO_CELULAR", "ID_TRANSACCION", "CODIGO_ARRIENDO", "SERIE"],
    "Datos Comerciales y Producto": ["TIPO_PIN", "PRODUCTO", "OPERADOR", "CANAL", "TIPO", "CANTIDAD"],
    "Información de la Empresa y Proveedor": ["EMPRESA", "PROVEEDOR", "SPT"],
    "Datos Económicos": ["COMISIÓN", "VALOR"]
}

# 5️⃣ Asignar cada columna única a una categoría
categorizadas = {categoria: [] for categoria in categorias}

for columna in columnas_unicas:
    asignada = False
    for categoria, palabras_clave in categorias.items():
        if any(palabra in columna.upper() for palabra in palabras_clave):  # Buscar coincidencias en mayúsculas
            categorizadas[categoria].append(columna)
            asignada = True
            break
    if not asignada:
        categorizadas.setdefault("Sin Categoría", []).append(columna)

# 6️⃣ Imprimir la categorización
print("\n📊 Categorización de Columnas Únicas:")
for categoria, columnas in categorizadas.items():
    print(f"\n📂 {categoria}:")
    for columna in columnas:
        print(f"- {columna}")

# 7️⃣ Guardar en un archivo de texto
ruta_txt = "categorias_columnas_unicas.txt"
with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write("📊 Categorización de Columnas Únicas:\n\n")
    for categoria, columnas in categorizadas.items():
        f.write(f"📂 {categoria}:\n")
        for columna in columnas:
            f.write(f"{columna}\n")
        f.write("\n")

print(f"\n✅ Archivo '{ruta_txt}' generado con éxito.")
