Listado de posibles tareas a desarrollar, agrupadas por subsistema.

Cada tarea está etiquetada según dificultad como:
 * Fácil (F)
 * Media (M)
 * Avanzada (A)

Autenticación
-------------
    * Autenticación por email (F)
    * Autenticación por certificado digital (A)
    * Autenticación con redes sociales (M)
    * Autenticación LDAP externo (M)

Censo
-----
    * Importación de censo desde excel (F)
    * Importación de censo de LDAP (M)
    * Exportación de censo (F)

Votaciones
----------
    * Definición/Administración Votación Sí/No (M)
    * Definición/Administración Varias preguntas en la misma votación (M)
    * Definición/Administración Votación por preferencia, definir una ordenación (M)

Cabina de votación
------------------
    * Implementar un cliente de escritorio, Gtk+, Qt, etc. (M)
    * Implementar clientes móviles, android, iphone, etc. (M)
    * Implementar una interfaz mejorada con tecnología javascript moderna,
      React, angular, etc. (M)
    * Interfaz de Votación Sí/No (M)
    * Interfaz de Varias preguntas en la misma votación (M)
    * Interfaz de Votación por preferencia, definir una ordenación (M)

Almacenamiento de votos (cifrados)
----------------------------------
    * Implementación con una base de datos no relacional (A)
    * Distribución y escalado con una base de datos distribuida / Cassandra (A)

Recuento / MixNet
-----------------
    * Optimizar cifrado, hacerlo multiproceso (M)
    * Implementar las pruebas de cero conocimiento (A)
    * Estudiar otros métodos de anonimización, otras mixnet con otros tipos
      de cifrado (A)

Post-procesado
--------------
    * Aplicar paridad a los resultados (F)
    * Aplicar la ley d'Hont (M)

Visualización de resultados
---------------------------
    * Pintado de gráficas y estudio de datos (F)
    * Mostrar información relevante en tiempo real, como el número de
      votos, porcentaje del censo, estadísticas de votantes, según
      perfiles, etc. (F)

Otras agrupaciones
==================

Integración
-----------
    * Versionar la API (F)
    * Autenticación entre servidores con token (M)
    * Implementar tests completos, mejorar la cobertura de código (M)
    * Implementar pruebas de rendimiento y benchmarks (M)
    * Definir scripts de despliegue automático con ansible (M)
    * Definir despliegue con docker para desarrollo y producción (M)

Seguridad
---------
    * Firmado y comprobación de código (tanto cliente como servidor) (A)
    * Protección contra ataques ddos (A)
    * Hacer todo el proceso distribuido para eliminar el punto único de
      fallo, censo distribuido, votos almacenados distribuidos y sólo
      se podrán en común para el recuento. (A)

Documentación
-------------
    * Completar documentación de API (F)
    * Completar documentación de todas las clases y funciones (F)

Traducciones
------------
    * Hacer la interfaz traducible (M)
    * Traducir la interfaz al español (F)
    * Traducir la interfaz a otros idiomas (F)

Diseño y usabilidad
-------------------
    * Estudiar la usabilidad y definir una nueva interfaz usable, con
      componentes css. (M)
    * Hacer la interfaz responsive, para que funcione en móviles. (M)
    * Estudiar la accesibilidad de la interfaz y hacerla accesible (M)
