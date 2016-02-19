#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Retencion():
    def __init__(self, retencion):
        self.retencion = retencion
        self.ruc = retencion.COH3_COIVID.COIV_CODPR.MAPV_RUC[0:-2]
        self.dv = retencion.COH3_COIVID.COIV_CODPR.MAPV_RUC[-1]
        self.nombre = retencion.COH3_COIVID.COIV_CODPR.MAPV_CODPER.MAPE_RAZON
        self.correoElectronico = retencion.COH3_COIVID.COIV_CODPR.MAPV_EMAIL
        self.pais = ""
        self.numeroComprobanteVenta = str(retencion.COH3_COIVID.COIV_NUMDOC)
        self.fechaComprobante = str(retencion.COH3_COIVID.COIV_DMADOC)[0:10]
        self.numeroTimbrado = str(retencion.COH3_COIVID.COIV_TIMBR)
        

        self.fechaRetencion = str(retencion.COH3_DMARET)[0:10]
        self.moneda = "PYG"
        #self.tipoCambio = 

    @property
    def situacion(self):
        if self.retencion.COH3_COIVID.COIV_CODPR.MAPV_RUC:
            situacion = 'contribuyente'
        else:
            if self.retencion.COH3_COIVID.COIV_CODPR.MAPE_DIRPR.MAPV_CODPER.MAPE_DIRPR:
                situacion = 'no contribuyente'
        return situacion

    @property
    def tipoIdentificacion(self):
        if self.situacion == 'contribuyente': return ""
        else :
            if self.retencion.COH3_COIVID.COIV_CODPR.MAPE_DIRPR.MAPV_CODPER.MAPE_TIDOC == 'CPY': return "CEDULA"
            elif self.retencion.COH3_COIVID.COIV_CODPR.MAPE_DIRPR.MAPV_CODPER.MAPE_TIDOC == 'PPY': return "PASAPORTE"
    
    @property
    def identificacion(self):
        if self.situacion == 'contribuyente': return ""
        else: return str(self.retencion.COH3_COIVID.COIV_CODPR.MAPE_DIRPR.MAPV_CODPER.MAPE_DOC)

    @property
    def domicilio(self):
        if self.situacion == 'contribuyente': return self.retencion.COH3_COIVID.COIV_CODPR.MAPV_CODPER.MAPE_DIRPR
        else: return ""
    @property
    def direccion(self):
        if self.situacion == 'contribuyente': return ""
        else: return self.retencion.COH3_COIVID.COIV_CODPR.MAPV_CODPER.MAPE_DIRPR
    @property
    def telefono(self):
        if self.situacion == 'contribuyente': return ""
        else: return str(self.retencion.COH3_COIVID.COIV_CODPR.MAPV_TELC)
    
    @property
    def condicionCompra(self):
        return "CONTADO"
    @property
    def cuotas(self):
        if self.condicionCompra == "CONTADO" : return 0
        else: return 0

    @property
    def tipoComprobante(self):
        if self.retencion.COH3_COIVID.COIV_TIPDOC == 1: return 1 #FACTURA
        elif self.retencion.COH3_COIVID.COIV_TIPDOC == 5: return 5 #AUTOFACTURA
        #11 ENTRADA A ESPECTACULOS PUBLICOS
 
    @property
    def numeroComprobanteVenta(self):
        return str(self.retencion.COH3_COIVID.COIV_NUMDOC)
    
    @property
    def detalle(self):
        lst=[]
        lst.append({ "cantidad" : 1, "tasaAplica" : "10", "precioUnitario" : 1080000, "descripcion" : "ALGO" })
        return lst

    @property
    def retencionRenta(self):
        if self.retencion.COH3_RETREN: return True
        else: return False
    @property
    def conceptoRenta(self):
        """ 
        Aquí debe ingresar el concepto de la retención (Solicite tabla de referencia a la institución)
        """
        if self.retencionRenta:
            if self.situacion == "contribuyente":
                #return"COMERCIAL_INDUSTRIAL_SERVICIO_REGISTRADO.1"
                return "PEQUENO_REGISTRADO.1"
                #return"SERVICIO_PERSONAL_REGISTRADO.1"
                #return"AGROPECUARIAS_REGISTRADO.1"
            elif self.situacion == "no contribuyente":
                return "COMERCIAL_INDUSTRIAL_SERVICIOS.1"
                #return "COMERCIAL_INDUSTRIAL_SERVICIOS.2"
                #return "COMERCIAL_INDUSTRIAL_SERVICIOS.3"
                #return "COMERCIAL_INDUSTRIAL_SERVICIOS.4"
                #return "COMERCIAL_INDUSTRIAL_SERVICIOS.5"
                #return "COMERCIAL_INDUSTRIAL_SERVICIOS.6"
                #return "PEQUENO.1"
                #return "SERVICIO_PERSONAL.1"
        else: return ""        

    @property
    def retencionIva(self):
        if self.retencion.COH3_RETIVA: return True
        else: return False
    
    @property
    def conceptoIva(self):
        if self.retencionIva:
            return "IVA.1" #Retenciones en carácter de pago a cuenta para Contribuyentes obligados por el impuesto
            #return "IVA.2" #Retenciones en carácter de Pago Único y Definitivo por acreditamiento de retribuciones a personas o entidades del exterior que no posean sucursales en el país
            #return "IVA.3" #Retenciones en carácter de Pago Único y Definitivo por la enajenación de bienes inmuebles, efectuados por aquellos designados como agentes de retención por la Administración Tributaria
            #return "IVA.4" #Retenciones en carácter de Pago Único y Definitivo por acreditamientos efectuados y no incluidos en los incisos anteriores
        else: return ""
    
    @property
    def rentaPorcentaje(self):
        """
        Aquí va el porcentaje a ser aplicado sobre la base imponible renta. Requerido.
        """
        #return 1
        #return 1.5
        #return 2
        #return 3
        #return 4.5
        #return 15
        #return 20
        #return 30
        return 0

    @property
    def rentaCabezasBase(self):
        """
        Aquí debe indicar el monto de la retención a ser aplicado sobre cada cabeza.
        """
        return 0
    @property
    def rentaCabezasCantidad(self):
        """
        Aqui debe indicar la cantidad de cabezas sobre la cual se aplicara la retencion
        """
        return 0
    @property
    def rentaToneladasBase(self):
        """
        Aqui debe indicar el monto de la retencion a ser aplicado sobre cada tonelada
        """
        return 0
    @property
    def rentaToneladasCantidad(self):
        """
        Aqui debe indicar la cantidad de toneladas sobre la cual se aplicara la retencion
        """
        return 0
    
    @property
    def ivaPorcentaje5(self):
        """
        Aqui va el porcentaje a ser aplicado sobre la base imponible del IVA 5 [0. 0.90909, 30, 50, 100]
        """
        return 30

    @property
    def ivaPorcentaje10(self):
        """
        Aqui va el porcentaje a ser aplicado sobre la base imponible del IVA 10 [0. 0.90909, 30, 50, 100]
        """
        return 30


