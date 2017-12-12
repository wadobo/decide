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
   servidores para hacer un recuento. https://verificatum.com/files/vmnv-3.0.2.pdf

 * Recuento, una vez obtenido el recuento en texto plano, con los datos
   anonimizados, se muestran los datos sobre la votación.

Puntos de extensión
===================

 * API:
    * Versionar la API
    * Autenticación entre servidores con token

 * Censo; Permitir autenticar de diferentes formas:
    * Autenticación por email
    * Autenticación por certificado digital
    * Autenticación con redes sociales
    * Autenticación LDAP externo

 * Tipo de votación:
    * Votación Sí/No
    * Varias preguntas en la misma votación
    * Votación por preferencia, definir una ordenación

 * Cifrado:
    * Optimizar cifrado, hacerlo multiproceso
    * Implementar las pruebas de cero conocimiento (difícil)
    * Estudiar otros métodos de anonimización, otras mixnet con otros tipos
      de cifrado

 * Tests:
    * Implementar tests completos, mejorar la cobertura de código
    * Implementar pruebas de rendimiento y benchmarks

 * Despliegue:
    * Definir scripts de despliegue automático con ansible
    * Definir despliegue con docker para desarrollo y producción

 * Documentación:
    * Completar documentación de API
    * Completar documentación de todas las clases y funciones

 * Traducciones:
    * Hacer la interfaz traducible
    * Traducir la interfaz al español
    * Traducir la interfaz a otros idiomas

 * Interfaz
    * Implementar una interfaz mejorada con tecnología javascript moderna,
      React, angular, etc.
    * Estudiar la usabilidad y definir una nueva interfaz usable, con
      componentes css.
    * Hacer la interfaz responsive, para que funcione en móviles.
    * Implementar un cliente de escritorio, Gtk+, Qt, etc.
    * Implementar clientes móviles, android, iphone, etc.

 * Postprocesado de votos:
    * Aplicar diferentes filtros sobre los resultados, aplicar condiciones,
      ponderaciones, paridad, etc
    * Estadísticas de votos, pintado de gráficas y estudio de datos

 * Meta-información:
    * Mostrar información relevante en tiempo real, como el número de
      votos, porcentaje del censo, estadísticas de votantes, según
      perfiles, etc.

 * Seguridad:
    * Firmado y comprobación de código (tanto cliente como servidor)
    * Protección contra ataques ddos
