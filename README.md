Python ChileAtiende:
====================
Esta es cliente escrito en Python que consume los servicios REST de la API para desarrolladores del sitio ChileAtiende.

Permite la integracion con los contenidos de este sitio, el cual está relacionado a los tramites que los servicios del Estado (instituciones publicas) publican a traves de él.

La API implementa los recursos como clases Python.

     Fichas
          obtener()
          listar()
          listarPorServicio()

     Servicios
          obtener()
          listar()

Ver las condiciones para el uso de la API de ChileAtiende en:

     https://www.chileatiende.cl/desarrolladores/politicasdeuso

Instalacion:
------------

Para instalar la API puedes hacer:

     $ pip install chileatiende

O descarga el paquete desde github e instalar manualmente:

     $ unzip python-chileatiende-master.zip
     $ cd python-chileatiende-master/
     $ python setup.py install

Ejemplo:
--------

Para el uso de la API se debe solicitar un token de acceso (access_token), para eso ir a la siguiente URL: 

     https://www.chileatiende.cl/desarrolladores/access_token

El siguente ejemplo accede al listado de servicios registrados en ChileAtiende.

     from chileatiende.cliente import Servicios
     
     access_token = 'PiKjQM1XAx1L4WiA'
     servicios = Servicios(access_token=access_token)
     
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
          print

La API cliente puede ser usada en cualquier framework python, como Tornado o Django. Incluso en Google App Engine.
Aqui un ejemplo:

     http://helloworld-rancavil.appspot.com/
