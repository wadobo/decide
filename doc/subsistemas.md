Definimos diferentes subsistemas que son más o menos independientes entre
sí y que se interconectan implementando una API concreta.

Cada subsistema se encarga de una tarea concreta en el sistema de voto.
Puede haber tareas que impliquen modificaciones en más de un subsistema,
por lo que habrá que coordinar el desarrollo para que puedan comunicarse
entre sí.

Subsistemas:
============

Autenticación
-------------

Autenticación de votantes. En una votación debemos autenticar a los
votantes y asegurarnos de que no se vota más de una vez o de que el votatne
puede votar en esa votación. Para ello debemos autenticar a la persona y
esta autenticación ha de ser segura, de tal forma que se reduzca la
posibilidad de fraude, suplantación de identidad, etc.

Posibles formas de autenticación:
    * Usuario / Contraseña
    * Enlace único por correo electrónico
    * Enlace único por SMS o sistema de mensajería (whatsapp, telegram, etc)
    * Certificado FNMT
    * Redes sociales (twitter, facebook, google)

Censo
-----

Una parte impmortante de una votación es el censo, que es el grupo de
personas que pueden votar en una votación. Gestoniar el censo es una tarea
importante a la hora de definir una votación y de controlar quién ha
votado y quién no.

El censo está relacionado con la autenticación, pero no es lo mismo, el
censo es la autorización para votar en una votación en concreto.

Votaciones
----------

Una votación puede definir una o varias preguntas, con diferente número de
opciones y diferentes configuraciones. Puede ser voto simple, ordenación de
una lista de opciones, elección múltiple, etc.

Cabina de votación
------------------

Interfaz para votar. Este subsistema se encarga de mostrar la interfaz de
voto de una votación en concreto, perimtiendo al votante votar de la forma
más sencilla posible.

Almacenamiento de votos (cifrados)
----------------------------------

Los votos se almacenan cifrados en una base de datos, donde tenemos la
relación directa de votante y voto. No se puede saber la intención de voto
porque el voto estará cifrado en la base de datos, pero sí tendremos la
información de quién ha votado y quién no.

Recuento / MixNet
-----------------

Susbsistema que se encarga de la parte criptográfica de una votación. La
mixnet es una red de ordenadores que generarán una clave compartida para
cifrar los votos. De esta manera sólo se podrá descifrar un voto cuando
todas las autoridades se pongan de acuerdo, a la hora de hacer el recuento.

En el proceso de recuento se desliga el votante del voto, cada autoridad
aplicará un paso de barajado de votos, antes de descifrar su parte, de tal
forma que cuando se obtenga el listado de votos en claro, no habrá forma de
saber qué ha votado cada usuario.

Post-procesado
--------------

Una vez realizado el recuento, tenemos una lista de números, este
subsistema de encarga de traducir esa lista de números a un resultado
coherente con el tipo de votación.

Por ejemplo, si es una votación de tipo simple, simplemente habrá que
contar el número de veces que aparece cada opción y se dará como ganadora
la opción con más opciones.

Este subsistema también es el encargado de aplicar diferentes reglas a los
resultados, por ejemplo, aplicar reglas de paridad, ley d'Hondt, etc.

Visualización de resultados
---------------------------

Este subsistema es el encargado de coger los datos obtenidos tras el post
procesado y pintarlos de una manera gráfica y entendible, generando
gráficas y tablas.

También se encargará de generar los diferentes informes necesarios de estos
resultados, ya sea en formato web, pdf, texto planto, etc.



Otras agrupaciones
==================

Además de estos subsistemas básicos hay tareas o desarrollos que no
pertenecen a ninguno de ellos y se pueden eglobar en los siguientes grupos:

Integración
-----------

Integración de todos los subsistemas para conseguir un único proyecto
funcional. Integración continua para ir integrando los diferentes cambios
de los subsistemas y detectar incompatibilidades lo antes posible, además
de pruebas de integración.

Seguridad
---------

Control de la seguridad de una votación completa, de todo el sistema de
voto o de partes de la votación.

Documentación
-------------

Documentación para votantes, administradores de votaciones y también
documentación de desarrollo.

Traducciones
------------

Traducción de la interfaz a diferentes idiomas.

Diseño y usabilidad
-------------------

Estudio y diseño de la interfaz de usuario atendiendo a criterios de diseño
y también de usabilidad para que el proceso de votación sea lo más
intuitivo posible, accesible para todo el mundo y que la herramienta no sea
un problema si no una solución.
