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

import httplib
import json
import xml.dom.minidom

class ChileAtiende:
	""" Clase base que se encarga de establecer la conexion al sitio de ChileAtiende
            Importante: Para poder hacer uso de los servicios REST provistos por la api
            de ChileAtiende es necesario obtener el access_token, pues toda comunicacion 
            se realiza teniendo este token.

            Para poder utilizar la interfaz de programacion de chile atiende se debe 
            solicitar un token de acceso a traves de la siguiente URL:
            
            https://www.chileatiende.cl/desarrolladores/access_token

            Para mas antecedentes de la api se puede revisar la siguiente URL:

            https://www.chileatiende.cl/desarrolladores
	"""
	def __init__(self,access_token=None):
		""" Constructor que inicializa la conexion al sitio de ChileAtiende """
		self._access_token = access_token
		self._url          = u'www.chileatiende.cl'
		self._connection   = httplib.HTTPSConnection(self._url)

	def _readDataFromConnection(self):
		""" Metodo privado que lee los datos desde la conexion establesida """
		response  = self._connection.getresponse()
		data      = response.read()
		if response.status != 200:
			mensaje = self._analizaRespuesta(data)
			raise Exception('Error : '+mensaje)
		return data

	def _json(self):
		""" Metodo privado que obtiene el resultado de GET URL en formato JSON """
		data      = self._readDataFromConnection()
		data_json = json.loads(data)

		return data_json

	def _xml(self):
		""" Metodo privado que obtiene el resultado de GET URL en formato XML """
		data     = self._readDataFromConnection()
		data_xml = xml.dom.minidom.parseString(data)

		return data_xml

	def _analizaRespuesta(self,response):
		html = xml.dom.minidom.parseString(response)
		h1   = html.getElementsByTagName('body')[0].getElementsByTagName('div')[0].getElementsByTagName('h1')[0].childNodes[0].nodeValue
		p    = html.getElementsByTagName('body')[0].getElementsByTagName('div')[0].getElementsByTagName('p')[0].childNodes[0].nodeValue
		mensaje = h1+" "+p
		return mensaje

class Fichas(ChileAtiende):
	""" La clase Fichas representa las Fichas de registro de los tramites disponibles
            a traves de ChileAtiende. Deriva de la clase base ChileAtiende.

            Ejemplo de uso:

            from chileatiende.clientes import Fichas

            fichas = Fichas(access_token=u'PiKjqM1XAx1P3Wia')
	"""
	def __init__(self,access_token=None):
		ChileAtiende.__init__(self,access_token)

	def obtener(self,fichaId=None,type='json',callback=''):
		""" Metodo que permite obtener una ficha de acuerdo a su identificador unico
		    fichaId. El metodo consume el servicio REST:

		    GET https://www.chileatiende.cl/api/fichas/{fichaId}

		    Nota: El valor por defecto de type es "json", esto indica que los datos
		    devueltos por el metodo estan en ese formato. Si type = "xml", los datos
		    son devueltos como un documento XML.
		"""
		self._connection.request('GET','/api/fichas/'+fichaId+'?access_token='+self._access_token+'&type='+type+'&callback='+callback)
		
		if type == 'json':
			self._ficha = self._json()
		else:
			self._ficha = self._xml()

		return self._ficha

	def listar(self,type='json',callback='',query='',maxResults=10,pageToken=''):
		""" Metodo que permite listar todas las fichas de los tramites registrados en ChileAtiende.
		    El metodo consume el servicio REST:

		    GET https://www.chileatiende.cl/api/fichas

		    Nota: El valor por defecto de type es "json", esto indica que los datos
		    devueltos por el metodo estan en ese formato. Si type = "xml", los datos
		    son devueltos como un documento XML.
		"""
		self._connection.request('GET','/api/fichas?access_token='+self._access_token+'&type='+type+'&callback='+callback+'&query='+query+'&maxResults='+str(maxResults)+'&pageToken='+pageToken)
		
		if type == 'json':
			self._fichas = self._json()
		else:
			self._fichas = self._xml()

		return self._fichas

	def listarPorServicio(self,servicioId=None,type='json',callback=''):
		""" Metodo que permite listar todas las fichas pertenencientes a un servicio publico.
		    El metodo consume el servicio REST:

		    GET https://www.chileatiende.cl/api/servicios/{servicioId}/fichas

		    Nota: El valor por defecto de type es "json", esto indica que los datos
		    devueltos por el metodo estan en ese formato. Si type = "xml", los datos
		    son devueltos como un documento XML.
		"""
		self._connection.request('GET','/api/servicios/'+servicioId+'/fichas?access_token='+self._access_token+'&type='+type+'&callback='+callback)
		
		if type == 'json':
			self._fichas = self._json()
		else:
			self._fichas = self._xml()

		return self._fichas

class Servicios(ChileAtiende):
	""" La clase Servicios representa a las instituciones que publican sus tramites (a traves de Fichas) 
	    en ChileAtiende. Deriva de las clase base ChileAtiende.

	    Ejemplo de uso:

	    from chileatiende.clientes import Servicios

	    servicios = Servicios(access_token=u'PiKjqM1XAx1P3Wia')
	"""
	def __init__(self,access_token=None):
		ChileAtiende.__init__(self,access_token)

	def obtener(self,servicioId=None,type='json',callback=''):
		""" Metodo que permite obtener los datos de un Servicio Publico, de acuerdo a su identificador 
		    unico servicioId. El metodo consume el servicio REST:

		    GET https://www.chileatiende.cl/api/servicios/{servicioId}

		    Nota: El valor por defecto de type es "json", esto indica que los datos
		    devueltos por el metodo estan en ese formato. Si type = "xml", los datos
		    son devueltos como un documento XML.
		"""
		self._connection.request('GET','/api/servicios/'+servicioId+'?access_token='+self._access_token+'&type='+type+'&callback='+callback)
		
		if type == 'json':
			self._servicio = self._json()
		else:
			self._servicio = self._xml()

		return self._servicio

	def listar(self,type='json',callback=''):
		""" Metodo que permite listar todos los servicios registrados en ChileAtiende.
		    El metodo consume el servicio REST:

		    GET https://www.chileatiende.cl/api/servicios

		    Nota: El valor por defecto de type es "json", esto indica que los datos
		    devueltos por el metodo estan en ese formato. Si type = "xml", los datos
		    son devueltos como un documento XML.
		"""
		self._connection.request('GET','/api/servicios?access_token='+self._access_token+'&type='+type+'&callback='+callback)
		
		if type == 'json':
			self._servicio = self._json()
		else:
			self._servicio = self._xml()

		return self._servicio