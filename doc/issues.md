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
    * Registro de usuarios. Formulario de registro que crea nuevos usuarios
    * Creación de API para usuarios
    * Autenticación con OAuth

Censo
-----
    * Frontend de administración de censo
    * Reutilización de censo entre diferentes votaciones
    * Grupos en censo para filtrado y agrupar
    * Importación de censo desde excel (F)
    * Importación de censo de LDAP (M)
    * Exportación de censo (F)

Votaciones
----------
    * Definición/Administración Votación Sí/No (M)
    * Definición/Administración Varias preguntas en la misma votación (M), afectaría al postprocesado, porque se tiene que mapear cada posible respuesta a un número y luego ese número se tiene que invertir.
    * Definición/Administración Votación por preferencia, definir una ordenación (M)
    * Almacenar tally y postprocesado en fichero del sistema y comprimir
    * URL de votación configurable/personalizable

Cabina de votación
------------------
    * Implementar un cliente de escritorio, Gtk+, Qt, etc. (M)
    * Implementar clientes móviles, android, iphone, etc. (M)
    * Implementar una interfaz mejorada con tecnología javascript moderna,
      React, angular, etc. (M)
    * Interfaz de Votación Sí/No (M)
    * Interfaz de Varias preguntas en la misma votación (M)
    * Interfaz de Votación por preferencia, definir una ordenación (M)
    * Interfaz de votación de telegram / slack / Matrix.org (Riot)
    * Usabilidad de cabina, que haya un proceso de votación, guiado

Almacenamiento de votos (cifrados)
----------------------------------
    * Implementación con una base de datos no relacional, mongodb (A)
    * Distribución y escalado con una base de datos distribuida / Cassandra (A)
    * Panel de control general, con información en tiempo real, por sexo, por IP/región. Esto está relacionado con el censo.
    * Edición del voto por el mismo votantes
    * Realización de backups
    * Alta disponibilidad

Recuento / MixNet
-----------------
    * Optimizar cifrado, hacerlo multiproceso (M)
    * Implementar las pruebas de cero conocimiento (A)
    * Estudiar otros métodos de anonimización, otras mixnet con otros tipos
      de cifrado (A)
    * Implementar una autoridad en otro lenguaje
    * Simplificar el cifrado, usar cifrado simétrico

Post-procesado
--------------
    * Aplicar paridad a los resultados (F)
    * Aplicar la ley d'Hont (M)
    * Aplicar algoritmo de recuento borda, esto afecta al módulo de votación
    * Soportar diferentes tipos de votación, multiples preguntas, etc

Visualización de resultados
---------------------------
    * Pintado de gráficas y estudio de datos (F)
    * Mostrar información relevante en tiempo real, como el número de
      votos, porcentaje del censo, estadísticas de votantes, según
      perfiles, etc. (F)
    * Implementar los diferentes tipos de votaciones
    * Implementar visualizaciones para diferentes plataformas, telegram, slack

Interfaz de administración
--------------------------

    * Implementar las llamadas API REST para administración
    * Interfaz propia para crear una votación completa
    * Gestión del censo

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
