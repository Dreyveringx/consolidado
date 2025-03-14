# Lista de términos originales
terminos = [
    "COLILLAS", "SERIE 1", "SERIE 2", "HORA", "VALOR", "Nro Anulación", "VENTA SIAC", "PREMIO SIAC",
    "%SIAC", "PAPELERÍA SIAC", "VENTA GTECH", "PREMIO GTECH", "% GTECH", "PREMIO ASTRO", "AJUSTE PREMIO",
    "AJUSTES VENTA SIACH", "AJUSTES VENTA GTECH", "AJUSTES VENTA ASTRO", "PREMIOS",
    "RESULTADOS DE LA LOTERIA 05 SORTEO 4734", "COLILLAS", "VENTA BRUTA", "VENTA NETA",
    "ID PROCESO", "NOMBRE PROCESO", "HORA INICIO", "HORA FIN", "TERMINAL", "USUARIO",
    "ESTADO", "#", "munic", "SPT", "COMISIÓN", "COMISIÓN LIQUIDA", "FESTIVO", "RECAUDO",
    "CUADRE DÍA", "AJUSTE DE VENTA", "AJUSTE RECAUDO", "SALDO", "LOQUI Nro", "USUARIO",
    "NOMBRE", "COLILLAS", "VENTA BRUTA", "VENTA NETA", "ANULADAS", "RIFAS", "RECARGAS",
    "CHANCE", "DOBLE PLAY", "SUPER CHANCE", "SUPERPLENO", "PLENO", "COMBINADO", "PATA", "UÑA"
]

# Eliminar duplicados
terminos_unicos = sorted(set(terminos))

# Categorizar términos
categorias = {
    "Transacciones y Ventas": ["VENTA SIAC", "VENTA GTECH", "VENTA BRUTA", "VENTA NETA", "AJUSTES VENTA SIACH", "AJUSTES VENTA GTECH", "AJUSTES VENTA ASTRO", "AJUSTE DE VENTA"],
    "Premios": ["PREMIO SIAC", "PREMIO GTECH", "PREMIO ASTRO", "AJUSTE PREMIO", "PREMIOS"],
    "Comisiones y Recaudos": ["COMISIÓN", "COMISIÓN LIQUIDA", "RECAUDO", "AJUSTE RECAUDO", "CUADRE DÍA"],
    "Juegos y Apuestas": ["CHANCE", "DOBLE PLAY", "SUPER CHANCE", "SUPERPLENO", "PLENO", "COMBINADO", "PATA", "UÑA", "RIFAS", "COLILLAZO"],
    "Anulaciones y Estados": ["Nro Anulación", "ANULADAS", "ESTADO"],
    "Datos del Proceso": ["ID PROCESO", "NOMBRE PROCESO", "HORA INICIO", "HORA FIN", "TERMINAL", "USUARIO"],
    "Información Adicional": ["RESULTADOS DE LA LOTERIA 05 SORTEO 4734", "FESTIVO", "SALDO"]
}

# Mostrar resultados organizados
for categoria, items in categorias.items():
    print(f"\n### {categoria} ###")
    for item in items:
        if item in terminos_unicos:
            print(f"{item}")
