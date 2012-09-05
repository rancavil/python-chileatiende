#!/usr/bin/env python
#
# Copyright 2012 Rodrigo Ancavil del Pino
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
	Este ejemplo consulta el listado de los servicios publicos (instituciones publicas)
	registrados en ChileAtiende.

	Importante: Para usar el API debes obtener el token de acceso (access_token) debes
	solicitarlo en:

	https://www.chileatiende.cl/desarrolladores/access_token

	En respuesta a tu solicitud se te enviara el codigo de acceso, el cual deberas utilizar
	al momento de usar el api.

	Importante: El codigo access_token de este ejemplo puede que no funcione!!!
	
"""

from chileatiende.cliente import Servicios

# El valor de access_token debe ser reemplazado por el codigo asignado por ChileAtiende
access_token = 'PiKjQM1XAx1L4WiA'
servicios = Servicios(access_token=access_token)

# El metodo listar() devolvera un objeto JSON (diccionario de python) con la estructura
# de datos para el registro de los servicios publicos.
# servicios : {
#		titulo : Titulo de la estructura de datos  
#		tipo   : chileatiende#serviciosFeed
#       items  : servicio : lista python con los servicios 
#				[{
#						url    : URL del sitio del servicio
#						nombre : Nombre del servicio
#						mision : Descripcion del servicio
#						id     : Identificado unico del servicio (servicioId)
#						sigla  : Sigla de la institucion
#                }]
# }
listaServicios = servicios.listar()

print 'serivicios : '
print '\ttitulo     :',listaServicios['servicios']['titulo']
print '\ttipo       :',listaServicios['servicios']['tipo']
print '\titems      : '
print '\t\tservicio : '
for servicio in listaServicios['servicios']['items']['servicio']:
	print '\t\t\turl    : ',servicio['url']
	print '\t\t\tnombre : ',servicio['nombre']
	print '\t\t\tmision : ',servicio['mision']
	print '\t\t\tid     : ',servicio['id']
	print '\t\t\tsigla  : ',servicio['sigla']