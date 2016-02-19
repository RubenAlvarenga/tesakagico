#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jsonschema import validate
import json
from datetime import datetime
import os, sys
sys.path += ['/usr/local/django-apps']
sys.path += [os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]]
os.environ['DJANGO_SETTINGS_MODULE'] = 'gico01_01.settingsBootstrap'
from gico01_01.gicov01.models import cohckretencion#, cohckcabecera, cohckagente, coivlibro

from collections import OrderedDict
from Retencion import Retencion
global schema
schema  = json.load(open("schema.js", 'r'))
global path_retencion
path_retencion = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]+"/tmp/json_retenciones/"


def getRetenciones(lst_ids_retenciones):
	lst=[]
	retenciones = cohckretencion.objects.filter(pk__in=lst_ids_retenciones)
	for r in retenciones:
		lst.append(Retencion(r))
	return lst
	

def getJsonRetenciones(retenciones):
	lst_jsonRetenciones=[]
	for r in retenciones:
		myjson = {
			"atributos": {
				"fechaCreacion":str(datetime.now())[0:10], 
				"fechaHoraCreacion":str(datetime.now())[0:19]
			},
			"informado": {
				"situacion" : r.situacion,
				"ruc" : r.ruc,
				"dv" : r.dv,
				"tipoIdentificacion" : r.tipoIdentificacion,
				"identificacion" : r.identificacion,
				"nombre" : r.nombre,
				"domicilio" : r.domicilio,
				"direccion" : r.direccion,
				"correoElectronico" : r.correoElectronico,
				"pais" : r.pais,
				"telefono" : r.telefono,
			},
			"transaccion" : {
				"condicionCompra" : r.condicionCompra,
				"cuotas" : r.cuotas,
				"tipoComprobante" : r.tipoComprobante,
				"numeroComprobanteVenta" : r.numeroComprobanteVenta,
				"fecha" : r.fechaComprobante,
				"numeroTimbrado" : r.numeroTimbrado,
			},
			"detalle" : r.detalle,
			"retencion" : {
				"fecha" : r.fechaRetencion,
				"moneda" : r.moneda,
				#"tipoCambio" : r.tipoCambio,
				"retencionRenta" : r.retencionRenta,
				"conceptoRenta" : r.conceptoRenta,
				"retencionIva" : r.retencionIva,
				"conceptoIva" : r.conceptoIva,
				"rentaPorcentaje" : r.rentaPorcentaje,
				"rentaCabezasBase" : r.rentaCabezasBase,
				"rentaCabezasCantidad" : r.rentaCabezasCantidad,
				"rentaToneladasBase" : r.rentaToneladasBase,
				"rentaToneladasCantidad" : r.rentaToneladasCantidad,
				"ivaPorcentaje5" : r.ivaPorcentaje5,
				"ivaPorcentaje10" : r.ivaPorcentaje10
			}
		}

		#validate(myjson, schema)
		lst_jsonRetenciones.append(myjson)
	return lst_jsonRetenciones


def jsontofile(lst_jsonRetenciones):
	with open(path_retencion+"retencion"+str(datetime.now())+".json", "w") as outfile:
		json.dump(lst_jsonRetenciones, outfile)





retenciones = getRetenciones([1999])
jsones=getJsonRetenciones(retenciones)
print jsones


jsontofile(jsones)





