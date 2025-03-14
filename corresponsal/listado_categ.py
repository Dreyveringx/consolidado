# Lista de términos originales
columnas = [
    "NOMBRE de colocador", "CANAL DE CONTRATACIÓN", "TIPO_USUARIO", "CANAL TRANSACCIONAL",
    "CANTIDAD", "COMISION (sin signo pesos)", "FECHA_TRANSACCION", "PAGADOR_DOCUMENTO",
    "PAGADOR_NOMBRE", "VALOR_FACTURA", "COD_PUNTO", "CANAL.1",
    "NOMBRES  nombre de quien figura en la factura, o pagador",
    "TIPO_USUARIO  (este campo se quita)??", "ID  (transacción)pte confirmar.",
    "NUMERO_DOC", "PRIMER_APELLIDO", "SEGUNDO_APELLIDO", "VALOR_SUBSIDIO",
    "USUARIO  (Cédula del vendedor)  SII", "COD_OFICINA", "NOMBRES del beneficiario.",
    "APELLIDOS del beneficiario", "OFICINA DE PAGO", "pin", "consecutivo", "valor",
    "fecha", "hora", "nota", "GIRO_TIPO", "NOMBRE_PROVEEDOR", "informacion_remitente",
    "beneficiario", "agencia_origen", "agencia_destino", "agencia_pago", "login",
    "NUMERO_COMPROBANTE", "estado", "proveedor", "CORREO DEL CLIENTE",
    "DOCUMENTO CLIENTE", "NOMBRE CLIENTE", "SUB PRODUCTO", "COMPROBANTE INGRESO",
    "AGENCIA", "CODIGO PRDUCTO", "FECHA TX2", "HORA TX3", "CODIGO VENDEDOR4",
    "CEDULA ASESORA5", "CODIGO DE ARRIENDO6", "TERMINAL7", "SPT8", "MUNICIPO9",
    "VALOR 10", "VALOR SIN IVA11", "ESTADO TX12", "ID TX13", "CJ", "CAJA", "COMPROBANTE",
    "FECHA COMPROBANTE", "NOMBRE USUARIO", "EMISIÓN (APLICA PARA RASPATODO)",
    "PAGUE (APLICA PARA BALOTO)", "SERIE 2", "CODIGO BARRAS", "CODIGO DE SEGURIDAD14",
    "PIN15", "ENCARGADO", "PRODUCTO", "RUTA", "APLICATIVO", "CAMPOS DINAMICOS",
    "PREMIOS - PAGOS", "NOMBRE DISTRIBUIDOR", "FECHA_VENTA", "FECHA_SORTEO",
    "COD_USUARIO/ DEBE QUEDAR (CAJA PAGO)", "COD_LOTERIA", "NOM_LOTERÍA",
    "COD_SORTEO DEBE QUEDAR /(NUM_SORTEO)", "COD_BARRAS(COMPLETO)", "NUM_APOSTADO",
    "SERIE_APOSTADA", "NUM_FRACCIÓN", "CANAL_VENTA", "TIPO_PREMIO", "TOTAL_PREMIO",
    "FECHA_PAGO", "HORA_PAGO", "DETALLE", "PROMOCIONALES PARA GELSA",
    "NOMBRE Y CODIGO DEL VENDEDOR", "FECHA DE VENTA", "CONCEPTO", "RETENCIÓN",
    "VENTA", "IVA", "BASE COMISIÓN", "COMISIÓN NETA", "RETENCION", "COMISIÓN",
    "ENTREGA", "REPORTE", "Apertura caja sivem", "Id Transaccion", "Tipo Transaccion",
    "Codigo Oficina", "Usuario", "Tipo identificacion cliente", "Oficina",
    "Codigo de oficina", "Zona", "Terminal", "Usuario.1", "Canal", "Codigo de arriendo",
    "Codigo de zona", "Nombres cliente", "Valor transaccion pesos",
    "Valor transaccion euros", "Valor transaccion dolares", "Fecha transaccion",
    "Nombre de la agencia", "Hora transaccion", "Cajero", "NETO", "tipo transaccion",
    "ID TRANSACCION", "CRUCE CON SUPER", "CRUCE CON PSL"
]

# Eliminar duplicados y filtrar valores no relevantes
columnas_unicas = sorted(set([col for col in columnas if not col.startswith("Unnamed")]))

# Clasificación de columnas
categorias = {
    "Datos del Cliente": ["NOMBRE CLIENTE", "DOCUMENTO CLIENTE", "CORREO DEL CLIENTE", 
                          "NOMBRES del beneficiario.", "APELLIDOS del beneficiario",
                          "PAGADOR_NOMBRE", "PAGADOR_DOCUMENTO", "NOMBRES cliente", 
                          "PRIMER_APELLIDO", "SEGUNDO_APELLIDO"],
    "Transacciones": ["ID TRANSACCION", "NUMERO_DOC", "FECHA_TRANSACCION", "HORA TX3",
                      "VALOR_FACTURA", "VALOR_SUBSIDIO", "VALOR 10", "VALOR SIN IVA11",
                      "TOTAL_PREMIO", "VALOR TRANSACTION PESOS", "VALOR TRANSACTION EUROS",
                      "VALOR TRANSACTION DOLARES"],
    "Venta y Comisiones": ["VENTA", "BASE COMISIÓN", "COMISIÓN", "COMISIÓN NETA", "RETENCIÓN",
                            "RETENCION", "IVA", "CODIGO PRDUCTO", "COD_LOTERIA"],
    "Puntos y Oficinas": ["OFICINA DE PAGO", "AGENCIA", "Nombre de la agencia",
                          "AGENCIA_ORIGEN", "AGENCIA_DESTINO", "AGENCIA_PAGO", "Zona",
                          "Codigo de oficina", "Codigo Oficina", "COD_PUNTO"],
    "Sistemas y Seguridad": ["LOGIN", "TERMINAL", "CAJA", "ENCARGADO", "APLICATIVO",
                              "CODIGO DE SEGURIDAD14"],
    "Juegos y Premios": ["TIPO_PREMIO", "PREMIOS - PAGOS", "COD_SORTEO DEBE QUEDAR /(NUM_SORTEO)",
                         "COD_BARRAS(COMPLETO)", "SERIE_APOSTADA", "NUM_APOSTADO", 
                         "NUM_FRACCIÓN", "FECHA_SORTEO", "CANAL_VENTA"],
    "Otros": ["DETALLE", "REPORTE", "CONCEPTO", "Apertura caja sivem", "Tipo Transaccion",
              "Codigo de arriendo", "CRUCE CON SUPER", "CRUCE CON PSL"]
}

# Mostrar resultados organizados
for categoria, items in categorias.items():
    print(f"\n### {categoria} ###")
    for item in items:
        if item in columnas_unicas:
            print(f"{item}")
