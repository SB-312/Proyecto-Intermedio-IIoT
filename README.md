# Proyecto Intermedio #1 – IIoT  
## Máquina de Almacenamiento con Brazo 3D Fischertechnik

## 1. Introducción

### 1.1 Resumen General
Este proyecto consiste en el diseño, construcción e implementación de un prototipo de **máquina de almacenamiento automatizada** utilizando el kit **Fischertechnik 3D Robot**. El sistema reproduce un proceso industrial simplificado de manipulación y almacenamiento, operando sobre un estante de 2×3 posiciones, actualmente validado en su primera columna.

El prototipo integra componentes de percepción, actuación y computación, aplicados al contexto del curso *Internet Industrial de las Cosas (IIoT) – Universidad de La Sabana, 2025-2*.

### 1.2 Motivación y Justificación
Los sistemas de almacenamiento automatizado (AS/RS) se utilizan en la industria moderna para mejorar eficiencia, trazabilidad y seguridad en el manejo de inventarios. La implementación de este prototipo tiene como objetivos:
- Reproducir un proceso de almacenamiento y recuperación a escala educativa.  
- Entrenar habilidades en control industrial e integración con IIoT.  
- Validar conceptos de automatización aplicados en un entorno de laboratorio.

### 1.3 Estructura de la Documentación
El documento está organizado en las siguientes secciones:  
1. Introducción: resumen, motivación y justificación.  
2. Solución propuesta: restricciones de diseño, arquitectura, criterios de diseño, diagramas.  
3. Configuración experimental, resultados y análisis.  
4. Autoevaluación.  
5. Conclusiones, retos y trabajo futuro.  
6. Referencias.  
7. Anexos.  

---

## 2. Solución Propuesta

### 2.1 Restricciones de Diseño
Los requerimientos fueron definidos siguiendo la norma ISO/IEC/IEEE 29148:2018.  

| Código | Requerimiento | Tipo | Prioridad | Descripción | Justificación |
|--------|---------------|------|-----------|-------------|---------------|
| R1 | Movimiento cartesiano en 3 ejes | Funcional | Alta | Posicionamiento en X, Y, Z | Requisito esencial del proceso |
| R2 | Manipulación de piezas | Funcional | Alta | Sujeción segura y liberación de piezas | Necesidad de almacenamiento confiable |
| R3 | Control mediante PLC 24 V | Técnico | Alta | Compatibilidad con estándar industrial | Formación orientada a industria 4.0 |
| R4 | Escalabilidad a estante completo | Escalabilidad | Media | Validación inicial en primera columna | Puede ampliarse con repuestos |
| R5 | Limitaciones de recursos | Restricción | Media | Sustitución de un eje faltante por actuador lineal | Asegura viabilidad del prototipo |
| R6 | Restricción económica | Económica | Media | Uso exclusivo de componentes disponibles | Restricción de presupuesto |
| R7 | Restricción de espacio | Espacio | Media | Base de montaje en tablero de madera | Condiciona el volumen de trabajo |
| R8 | Tiempo de desarrollo | Temporal | Alta | Entrega en plazo académico (22/08/2025) | Condiciona el alcance de la solución |

### 2.2 Arquitectura Propuesta
El sistema se compone de:
- **Percepción:** finales de carrera para detección de límites en los ejes.  
- **Actuación:** motores DC con tornillo sin fin y motorreductores para desplazamientos y prensión.  
- **Computación:** PLC Siemens LOGO! 24 V, programado en ladder diagram.  
- **Conectividad (futura):** integración prevista con protocolos Modbus/MQTT.  

Se recomienda incluir el diagrama de bloques en `/docs/arquitectura.png`.

### 2.3 Desarrollo Teórico Modular y Criterios de Diseño
- Modularidad: cada eje (X, Y, Z) y el gripper se consideran subsistemas independientes.  
- Robustez: finales de carrera aseguran operación segura y evitan daños por sobrecarrera.  
- Escalabilidad: el sistema puede extenderse al estante completo con componentes adicionales.  

### 2.4 Diagramas UML
Se recomienda elaborar:  
- Diagrama de casos de uso: interacción del operador con el sistema.  
- Diagrama de clases: módulos de software PLC.  
- Diagrama de secuencia: ciclo de almacenamiento y recuperación.  

Los diagramas deben ubicarse en `/docs/uml/`.

### 2.5 Esquemáticos de Hardware
El sistema debe incluir el esquemático de conexión de motores, finales de carrera y PLC. Se adjuntará en `/docs/esquematico.pdf`.

### 2.6 Estándares de Ingeniería Aplicados
- ISO/IEC/IEEE 29148:2018 para gestión de requerimientos.  
- Buenas prácticas de documentación IEEE.  
- Normativas de seguridad eléctrica para sistemas de 24 V DC.  

---

## 3. Configuración Experimental, Resultados y Análisis

### 3.1 Protocolo de Pruebas
1. Calibración y homing de los ejes mediante finales de carrera.  
2. Ciclo de toma y depósito de pieza en primera columna.  
3. Recuperación de pieza desde estante.  
4. Repetición de ciclos para validar estabilidad.  

### 3.2 Resultados
- Posicionamiento estable en los tres ejes.  
- Manipulación de piezas con la pinza funcional y confiable.  
- Operación limitada al primer módulo del estante debido a restricción mecánica.  

### 3.3 Análisis
El prototipo cumple con la funcionalidad principal de almacenamiento y recuperación. La confiabilidad en la repetición de ciclos es satisfactoria. La falta de un eje original fue mitigada exitosamente mediante un actuador lineal, sin comprometer los objetivos principales.

---

## 4. Autoevaluación
- **Fortalezas:** prototipo funcional, documentación estructurada, operación validada.  
- **Debilidades:** capacidad parcial del estante, conectividad IIoT aún no implementada.  
- **Mejoras futuras:** optimización del programa en PLC, integración con dashboard remoto.  

---

## 5. Conclusiones y Trabajo Futuro
Se construyó un prototipo funcional de máquina de almacenamiento, aplicando conceptos de automatización e IIoT. El sistema es escalable y permite futuras ampliaciones.  
El trabajo futuro contempla:  
- Ampliar operación a estante completo.  
- Implementar conectividad con Node-RED y MQTT.  
- Medir métricas de rendimiento (tiempo de ciclo, precisión, confiabilidad).  

---

## 6. Referencias
- Fischertechnik, “PLC programming.” Disponible en: https://www.fischertechnik.de/en/industry-and-universities/plc-programming  
- ISO/IEC/IEEE 29148:2018 – Systems and software engineering — Life cycle processes — Requirements engineering.  
- Literatura técnica sobre sistemas AS/RS e integración de IIoT en procesos logísticos.  

---

## 7. Anexos
- Código fuente PLC (`/src/programa_plc.lad`).  
- Diagramas UML (`/docs/uml/`).  
- Esquemáticos de hardware (`/docs/esquematico.pdf`).  
- Protocolo de pruebas detallado (`/tests/protocolo_pruebas.md`).  
- Presentación de sustentación (`/media/presentacion.pdf`).  

**Nota:** La demostración del prototipo se realizará en presentación presencial, por lo cual no se incluye video.
