{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "/",
    "type": "object",
    "required": ["atributos", "informado", "transaccion", "detalle", "retencion"],
    "properties": {
        "atributos": {
            "id": "atributos",
            "type": "object",
            "properties": {
                "fechaCreacion": {
                    "id": "fechaCreacion",
                    "type": "string",
                    "format": "date"
                },
                "fechaHoraCreacion": {
                    "id": "fechaHoraCreacion",
                    "type": "string"
                }
            },
            "required": ["fechaCreacion", "fechaHoraCreacion"],
            "additionalProperties": false
        },
        "informado": {
            "id": "informado",
            "type": "object",
            "properties": {
                "situacion": {
                    "id": "situacion",
                    "type": "string",
                    "enum": ["contribuyente", "no contribuyente", "no domiciliado"],
                    "description": " Aqui debe informar la situacion del proveedor"
                },
                "ruc": {
                    "id": "ruc",
                    "type": ["string", "null"],
                    "description": "Aqui debe ingresar el RUC del contribuyente"
                },
                "dv": {
                    "id": "dv",
                    "type": ["string", "null"],
                    "description": " Aqui debe ingresar el digito verificador el ruc"
                },
                "tipoIdentificacion": {
                    "id": "tipoIdentificacion",
                    "type": ["string", "null"],
                    "enum": ["CEDULA", "CARNE_RESIDENCIA", "PASAPORTE", ""],
                    "description": "En caso que el informado sea no contribuyente o no domiciliado aqui debe informar que tipo de documento de identificacion utilizara"
                },
                "identificacion": {
                    "id": "identificacion",
                    "type": ["string", "null"],
                    "description": "En caso que el informado sea no contribuyente o no domiciliado aqui debe informar su numero de documento de identificacion"
                },
                "nombre": {
                    "id": "nombre",
                    "type": "string",
                    "description": "Nombre completo del informado"
                },
                "domicilio": {
                    "id": "domicilio",
                    "type": ["string", "null"],
                    "description": "Para el caso de un informado contribuyente, aqui debe especificar cual es su domicilio"
                },
                "direccion": {
                    "id": "direccion",
                    "type": ["string", "null"],
                    "description": "Para un caso de un informado no contribuyente o no domiciliado, aqui debe especificar su direccion"
                },
                "correoElectronico": {
                    "id": "correoElectronico",
                    "type": ["string", "null"],
                    "description": "Para un caso de un informado no contribuyente o no domiciliado, aqui debe especificar su direccion de correo electronico"
                },
                "pais": {
                    "id": "pais",
                    "type": ["string", "null"],
                    "description": "Para un caso de un informado no domiciliado, aqui debe especificar su pais de origen"
                },
                "telefono": {
                    "id": "telefono",
                    "type": ["string", "null"],
                    "description": "Para un caso de un informado no contribuyente o no domiciliado, aqui debe especificar su numero de telefono"
                }
            },
            "required": ["situacion", "identificacion", "nombre", "domicilio", "direccion", "correoElectronico", "pais", "telefono"],
            "additionalProperties": false
        },
        "transaccion": {
            "id": "transaccion",
            "type": "object",
            "properties": {
                "condicionCompra": {
                    "id": "condicionCompra",
                    "type": "string",
                    "enum": ["CONTADO", "CREDITO"],
                    "description": " Aqui debe informar la condicion de compra "
                },
                "cuotas": {
                    "id": "cuotas",
                    "type": "integer",
                    "description": "En caso de una condicion de compra CREDITO especificar la cantidad de cuotas"
                },
                "tipoComprobante": {
                    "id": "tipoComprobante",
                    "type": "integer",
                    "description": "Codificacion de tipo de comprobante (Solicite la tabla de referencia a la Institucion)"
                },
                "numeroComprobanteVenta": {
                    "id": "numeroComprobanteVenta",
                    "type": "string",
                    "description": "Aqui debe ingresar en numero del comprobante de venta sobre la cual se practicara la retencion"
                },
                "fecha": {
                    "id": "fecha",
                    "type": "string",
                    "format": "date",
                    "description": " Aqui debe ingresar la fecha del comprobante de venta"
                },
                "numeroTimbrado": {
                    "id": "numeroTimbrado",
                    "type": "string",
                    "description": "Aqui debe ingresar en numero de timbrado del comprobante de venta"
                }
            },
            "required": ["condicionCompra", "tipoComprobante", "numeroComprobanteVenta", "fecha", "numeroTimbrado"],
            "additionalProperties": false
        },
        "detalle": {
            "id": "detalle",
            "type": "array",
            "items": {
                "id": "detalle",
                "type": "object",
                "properties": {
                    "cantidad": {
                        "id": "cantidad",
                        "type": "number",
                        "description": "Cantidad de items"
                    },
                    "tasaAplica": {
                        "id": "tasaAplica",
                        "type": "string",
                        "enum": ["0", "5", "10"],
                        "description": "Se debe indicar la tasa que se aplica al item (exento(0), 5% o 10%)"
                    },
                    "precioUnitario": {
                        "id": "precioUnitario",
                        "type": "number",
                        "description": "Valor del Precio de un item"
                    },
                    "descripcion": {
                        "id": "descripcion",
                        "type": "string",
                        "description": "Descripción de la fila de detalle"
                    }
                },
                "required": ["tasaAplica", "cantidad", "precioUnitario", "descripcion"],
                "additionalProperties": false
            },
            "additionalItems": false
        },
        "retencion": {
            "id": "retencion",
            "type": "object",
            "properties": {
                "fecha": {
                    "id": "fecha",
                    "type": "string",
                    "format": "date",
                    "description": "Aqui debe ingresar la fecha de la retencion"
                },
                "moneda": {
                    "id": "moneda",
                    "type": "string",
                    "description": "Aquí debe informar en que moneda se encuentra la operación",
                    "enum": ["EUR", "PYG", "USD", "BRL"]
                },
                "tipoCambio": {
                    "id": "tipoCambio",
                    "type": "number",
                    "description": "Aquí debe informar el tipo de cambio a utilizar según la moneda antes informada"
                },
                "retencionRenta": {
                    "id": "retencionRenta",
                    "type": "boolean",
                    "description": "Verdadero / Falso indicando si se retiene renta"
                },
                "conceptoRenta": {
                    "id": "conceptoRenta",
                    "type": "string",
                    "description": "Aqui debe ingresar el concepto de la retencion (Solicite table de referencia a la institucion)"
                },
                "retencionIva": {
                    "id": "retencionIva",
                    "type": "boolean",
                    "description": "Indica si se retiene el IVA"
                },
                "conceptoIva": {
                    "id": "conceptoIva",
                    "type": "string",
                    "description": "Aqui debe ingresar el concepto de la retencion para el IVA (Solicite table de referencia a la institucion)"
                },
                "rentaPorcentaje": {
                    "id": "rentaPorcentaje",
                    "type": "number",
                    "enum": [0, 30, 10, 3],
                    "description": "Aqui va el porcentaje a ser aplicado sobre la base imponibe renta"
                },
                "rentaCabezasBase": {
                    "id": "rentaCabezasBase",
                    "type": "integer",
                    "description": "Aqui debe indicar el monto de la retencion a ser aplicado sobre cada cabeza"
                },
                "rentaCabezasCantidad": {
                    "id": "rentaCabezasCantidad",
                    "type": "integer",
                    "description": "Aqui debe indicar la cantidad de cabezas sobre la cual se aplicara la retencion"
                },
                "rentaToneladasBase": {
                    "id": "rentaToneladasBase",
                    "type": "integer",
                    "description": "Aqui debe indicar el monto de la retencion a ser aplicado sobre cada tonelada"
                },
                "rentaToneladasCantidad": {
                    "id": "rentaToneladasCantidad",
                    "type": "integer",
                    "description": "Aqui debe indicar la cantidad de toneladas sobre la cual se aplicara la retencion"
                },
                "ivaPorcentaje5": {
                    "id": "ivaPorcentaje5",
                    "type": "number",
                    "enum": [0, 100, 50, 30],
                    "description": "Aqui va el porcentaje a ser aplicado sobre la base imponible del IVA 5"
                },
                "ivaPorcentaje10": {
                    "id": "ivaPorcentaje10",
                    "type": "number",
                    "enum": [0, 100, 50, 30],
                    "description": "Aqui va el porcentaje a ser aplicado sobre la base imponibe del IVA 10"
                }
            },
            "required": ["fecha", "retencionRenta", "moneda", "ivaPorcentaje5", "ivaPorcentaje10", "rentaCabezasBase", "rentaCabezasCantidad", "rentaToneladasBase", "rentaToneladasCantidad", "retencionIva", "conceptoIva", "rentaPorcentaje"],
            "additionalProperties": false
        }
    },
    "additionalProperties": false
}