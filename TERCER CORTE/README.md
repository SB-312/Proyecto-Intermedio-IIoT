# PROYECTO INTERMEDIO IIOT #3
Christian Daniel Morales Jimenez, Maria Alejandra Cabrera Arauz, Juan Diego Lemus Rey

## 1. Resumen General, Motivación y Estructura del Documento

### 1.1 Resumen General
El presente documento describe el diseño, desarrollo e integración del Gemelo Digital del módulo High Bay Storage de Fischertechnik, realizado como proyecto final del curso Internet Industrial de las Cosas (IIoT). El trabajo se desarrolló de manera progresiva a lo largo de los tres cortes del semestre, consolidando al final una solución integral que combina automatización física, visualización digital, conectividad industrial y modelación de participación dentro de una fábrica inteligente.

Durante el Primer Corte, se analizó el proceso industrial del sistema de almacenamiento automático, identificando la lógica de operación, los eventos críticos, los flujos de trabajo y los requisitos de control necesarios. En el Segundo Corte, se implementó la base del Gemelo Digital: la automatización del módulo mediante actuadores, la integración de sensores, la estructura de comunicación con el PLC emulado y el desarrollo inicial de la interfaz digital que representó el comportamiento del proceso.

Finalmente, en el Tercer Corte, se integró la solución completa. Esto incluyó la incorporación de simulaciones adicionales para resolver limitaciones físicas del kit, el diseño y fabricación de elementos externos requeridos para asegurar la compatibilidad mecánica del proceso, la conexión en tiempo real entre el modelo físico y digital mediante protocolos industriales, y la validación final del sistema.

Como resultado, se obtuvo un sistema capaz de operar el módulo High Bay Storage de forma completamente automatizada, visualizar su estado operativo en tiempo real y participar dentro del modelo de una Fábrica Inteligente, correspondiente al curso de IIoT del semestre 2025-2. En este entorno colaborativo, nuestro módulo cumple el rol de punto inicial del flujo productivo: selecciona el producto y posteriormente lo pone en la basa para entrega al siguiente equipo que se encarga del transporte hacia la máquina de clasificación.

### 1.2 Motivación
La industria está migrando hacia modelos de automatización más flexibles, conectados y capaces de operar con información en tiempo real, es por eso que los gemelos digitales y el IoT toman un papel fundamental, pues permiten anticipar fallas, optimizar recursos y validar decisiones antes de implementar cambios en el entorno físico. Durante los tres cortes trabajamos con la plataforma Fischertechnik ya que facilita la experimentación con procesos industriales reales a pequeña escala. 

La motivación principal fue lograr una solución completa que incorporara no solo la automatización, sino también elementos de IIoT. Es importante resaltar que varios comportamientos del módulo no pueden simularse o resolverse únicamente con las fichas estándar por lo que se diseño soportes, simulaciones y adaptaciones externas, motivando un enfoque ingenieril más creativo y completo. Además, el enfoque del curso, incrementando los resultados por cortes motivó a estructurar la solución desde cero, con entregables funcionales en cada etapa y un producto final completamente integrado.

### 1.3 Justificación
Durante el desarrollo del proyecto se identificaron varias necesidades que justificaron el enfoque adoptado. Primero, integrar un modelo físico con un modelo digital permitió comprender y aplicar de manera práctica los principios de IIoT, incluyendo comunicación industrial, monitoreo distribuido y conectividad. Segundo, la naturaleza modular del High Bay Storage exigió resolver limitaciones técnicas no contempladas en los kits originales, tales como "productos" compatibles con el sistema, la simulación del comportamiento de sensores externos y la adaptación física del entorno para lograr una detección confiable. Estas necesidades impulsaron un proceso de diseño ingenieril real, en el que fue necesario proponer, validar y ajustar soluciones tanto en hardware como en software.

Por otro lado, la estructura del repositorio permitió documentar la evolución del proyecto y mantener control sobre cada fase. El Tercer Corte consolida toda la solución final, integrando el PLC emulado, la HMI, el sistema embebido para comunicación, el gemelo digital y las pruebas de interacción con otros equipos. En conjunto, el proyecto demuestra una solución integral, escalable y alineada con los requerimientos establecidos para la implementación de un Gemelo Digital funcional y su participación en un modelo de Fábrica Inteligente.

### 1.4 Estructura de la Documentación
La documentación se organiza para reflejar el proceso completo del proyecto:

- En la Sección 1 se presenta el contexto general, la motivación del trabajo, su importancia y cómo está estructurado el documento.
- La Sección 2 describe la solución propuesta: restricciones identificadas, arquitectura del sistema y las decisiones de diseño tanto de hardware como de software.
- En la Sección 3 se detalla el desarrollo modular completo.
- La Sección 4 explica la configuración experimental, los resultados obtenidos y el análisis comparativo entre el gemelo digital y el prototipo físico.
- La Sección 5 presenta la autoevaluación del protocolo de pruebas y las mejoras que surgieron a partir de las validaciones.
- La Sección 6 incluye conclusiones, retos enfrentados, recomendaciones para trabajo futuro y las referencias consultadas.

Finalmente, los Anexos distribuidos en diferentes carpetas contienen el código fuente documentado, esquemáticos, diseños físicos y material complementario, junto con el video demostrativo que resume el funcionamiento de la solución.

### 1.5 Roles y Contribuciones

| Categoría             | Criterio                                                                     | Responsable |
|-----------------------|------------------------------------------------------------------------------|-------------|
| Gestión de proyecto   | Repositorio Git creado                                                       | Maria Alejandra Cabrera Arauz   |
| Gestión de proyecto   | Estructura de carpetas estandarizada (src/ hmi/ docs/ proto/ video/)         | Maria Alejandra Cabrera Arauz   |
| Gestión de proyecto   | Tablero con Roles y contribuciones por integrante                            | Maria Alejandra Cabrera Arauz   |
| Diseño ingenieril     | Diseño y desarrollo de soluciones complementarias para resolver limitaciones | Maria Alejandra Cabrera Arauz   |
| Wiki técnica          | Resumen General, Motivación y Estructura del Documento                       | Maria Alejandra Cabrera Arauz   |
| Wiki técnica          | Declaración del uso de IA y fuentes bibliográficas                           | Todos  |
| Video (≤10 min)       | Demostración y explicación clara (sim + prototipo + E-Stop + anomalía)       | Todos  |

---

## 2. Solución Propuesta

### 2.1 Restricciones de Diseño Identificadas

### 2.2 Arquitectura Propuesta

#### 2.2.1 Arquitectura de Hardware
Diagrama de bloques del hardware:

#### 2.2.2 Arquitectura de Software
Diagrama de bloques del software: 

---

## 3. Desarrollo Teórico y Modular

### 3.1 Criterios de Diseño Establecidos

### 3.2 UML de la Solución Completa
- Diagrama de casos de uso:
- Diagrama de clases:
- Diagrama de secuencia por módulos:
- Diagrama de componentes:

### 3.3 Desarrollo por Módulos de Software

### 3.4 Esquemáticos de Hardware Diseñados

### 3.5 Estándares de Ingeniería Aplicados
Normativas y buenas prácticas utilizadas:

---

## 4. Configuración Experimental, Resultados y Análisis

### 4.1 Configuración Experimental 

### 4.2 Resultados

### 4.3 Análisis

---

## 5. Autoevaluación del Protocolo de Pruebas

---

## 6. Conclusiones, Retos, Trabajo Futuro y Referencias

### 6.1 Conclusiones

### 6.2 Retos Presentados

### 6.3 Trabajo Futuro

### 6.4 Referencias y uso de IA

