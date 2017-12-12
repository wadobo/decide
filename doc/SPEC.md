Plataforma voto electrónico educativa
=====================================

El objetivo de este proyecto es implementar una plataforma de voto
electrónico seguro, que cumpla una serie de garantías básicas, como la
anonimicidad y el secreto del voto.

Se trata de un proyecto educativo, pensado para el estudio de sistemas de
votación, por lo que primará la simplicidad por encima de la eficiencia
cuando sea posible. Por lo tanto se asumen algunas carencias para permitir
que sea entendible y extensible por alumnos.

Propuesta técnica
=================

Aplicación completa implementada en python, que se publicará en un
repositorio público, en github, permitiendo la colaboración desde el
primer momento.

Utilización del framework Django para implementar toda la aplicación, con
el mínimo número de dependencias externas para que la instalación y
desarrollo sea lo más fácil posible.

API rest para comunicación con clientes y entre servidores, en el caso de
votaciones con varias autoridades.

Para la parte de cifrado se utilizará la implementación sencilla en python
de una mixnet, que mezcla y recifra los votos, asegurando la anonimicidad
de los mismos. Sin embargo, esta implementación no provee las pruebas de
cero conocimiento para verificar a posteriori.

Interfaz en html plano, con javascript simple para cifrado de votos en
cliente.

La aplicación se compondrá de diferentes módulos básicos:

 * Votación, en principio se podrá definir sólo una pregunta por votación,
   con una serie de opciones y sólo se podrá elegir una.

 * Censo, autenticación y permisos para votar, en principio se usará la
   autenticación de django.

 * Mixnet, generación de claves de votación y sincronización entre
   servidores para hacer un recuento.
    * https://verificatum.com/files/vmnv-3.0.2.pdf
    * https://github.com/danigm/avmixnet

 * Recuento, una vez obtenido el recuento en texto plano, con los datos
   anonimizados, se muestran los datos sobre la votación.

Puntos de extensión
===================

Cada tarea está etiquetada según dificultad como:
 * Fácil (F)
 * Media (M)
 * Avanzada (A)

 * API:
    * Versionar la API (F)
    * Autenticación entre servidores con token (M)

 * Censo; Permitir autenticar de diferentes formas:
    * Autenticación por email (F)
    * Autenticación por certificado digital (A)
    * Autenticación con redes sociales (M)
    * Autenticación LDAP externo (M)

 * Tipo de votación:
    * Votación Sí/No (M)
    * Varias preguntas en la misma votación (M)
    * Votación por preferencia, definir una ordenación (M)

 * Cifrado:
    * Optimizar cifrado, hacerlo multiproceso (M)
    * Implementar las pruebas de cero conocimiento (A)
    * Estudiar otros métodos de anonimización, otras mixnet con otros tipos
      de cifrado (A)

 * Tests:
    * Implementar tests completos, mejorar la cobertura de código (M)
    * Implementar pruebas de rendimiento y benchmarks (M)

 * Despliegue:
    * Definir scripts de despliegue automático con ansible (M)
    * Definir despliegue con docker para desarrollo y producción (M)

 * Documentación:
    * Completar documentación de API (F)
    * Completar documentación de todas las clases y funciones (F)

 * Traducciones:
    * Hacer la interfaz traducible (M)
    * Traducir la interfaz al español (F)
    * Traducir la interfaz a otros idiomas (F)

 * Interfaz
    * Implementar una interfaz mejorada con tecnología javascript moderna,
      React, angular, etc. (M)
    * Estudiar la usabilidad y definir una nueva interfaz usable, con
      componentes css. (M)
    * Hacer la interfaz responsive, para que funcione en móviles. (M)
    * Implementar un cliente de escritorio, Gtk+, Qt, etc. (M)
    * Implementar clientes móviles, android, iphone, etc. (M)

 * Postprocesado de votos:
    * Aplicar diferentes filtros sobre los resultados, aplicar condiciones,
      ponderaciones, paridad, etc (F)
    * Estadísticas de votos, pintado de gráficas y estudio de datos (F)

 * Meta-información:
    * Mostrar información relevante en tiempo real, como el número de
      votos, porcentaje del censo, estadísticas de votantes, según
      perfiles, etc. (F)

 * Seguridad:
    * Firmado y comprobación de código (tanto cliente como servidor) (A)
    * Protección contra ataques ddos (A)
    * Hacer todo el proceso distribuido para eliminar el punto único de
      fallo, censo distribuido, votos almacenados distribuidos y sólo
      se podrán en común para el recuento. (A)
