# Proyecto Intermedio #1 – IIoT

## Máquina de Almacenamiento con Robot 3D Fischertechnik

---

## 1. Introducción

### 1.1 Resumen General

Este proyecto corresponde a la **construcción, programación y validación** de un prototipo de máquina de almacenamiento automatizada basado en el modelo **High Bay Storage Rack** de Fischertechnik.
El sistema es un **robot cartesiano de tres ejes (X, Y, Z)** que utiliza un carro deslizable para depositar y recoger piezas en un **estante de 2×3 posiciones**.

Actualmente, por limitaciones de repuestos, se validó solo la **primera columna del estante**, pero el diseño es **escalable** al resto de las posiciones. El control se desarrolló con el **ROBO TX Automation Robots** programado en **ROBO Pro Coding**, gestionando motores y sensores de final de carrera.

### 1.2 Motivación y Justificación

Los sistemas AS/RS son esenciales en la logística moderna e Industria 4.0. El presente prototipo permite:

* Comprender la **mecánica de robots cartesianos**.
* Desarrollar **habilidades en control de motores, sensores y rutinas de referencia**.
* Practicar la **resolución de problemas reales de ensamble**.
* Integrar hardware y software en un entorno educativo.

### 1.3 Estructura del Documento

1. Introducción
2. Solución propuesta
3. Configuración experimental, resultados y análisis
4. Programación en ROBO Pro Coding
5. Avances constructivos documentados
6. Autoevaluación
7. Conclusiones y trabajo futuro
8. Referencias
9. Anexos

---

## 2. Solución Propuesta

### 2.1 Restricciones de Diseño

| Código | Restricción / Requerimiento                        | Tipo          | Impacto |
| -----: | -------------------------------------------------- | ------------- | ------- |
|     R1 | Movimiento cartesiano en 3 ejes (X, Y, Z)          | Funcional     | Alta    |
|     R2 | Operación en **9 V** (no 24 V estándar industrial) | Técnica       | Alta    |
|     R3 | Faltan ejes de **260 mm (Art.-No. 107436)**        | Mecánica      | Alta    |
|     R4 | Sustitución de un eje por **actuador lineal**      | Restricción   | Media   |
|     R5 | Adaptación con motorreductores alternativos        | Técnica       | Media   |
|     R6 | Limitación de baterías 9 V para pruebas            | Operativa     | Media   |
|     R7 | Operación solo en la primera columna del estante   | Escalabilidad | Media   |
|     R8 | Tiempo de entrega corto                            | Temporal      | Alta    |

---

### 2.2 Arquitectura Física

```mermaid
flowchart TB
  subgraph Robot["Robot cartesiano 3 ejes"]
    X["Eje X - motor M1 (movimiento horizontal)"]
    Z["Eje Z - motor M3 / actuador lineal (movimiento vertical)"]
    Y["Eje Y - motor M2 (carro deslizable)"]

    FXmin["Final de carrera X-"]
    FXmax["Final de carrera X+"]

    FZmin["Final de carrera Z-"]
    FZmax["Final de carrera Z+"]

    FYmin["Final de carrera Y-"]
    FYmax["Final de carrera Y+"]

    FXmin --- X --- FXmax
    FZmin --- Z --- FZmax
    FYmin --- Y --- FYmax
  end

  subgraph Estante["Estante de almacenamiento 2×3"]
    S11["Slots de almacenamiento"]
  end

  subgraph PuntoExt["Punto de recolección/entrega"]
    P11["Estación de entrada/salida"]
  end

  Y --> S11
  Y --> P11
```

---

### 2.3 Criterios de Diseño

* **Modularidad:** cada eje es independiente y ensamblado por etapas.
* **Adaptación:** reemplazo de piezas ausentes por soluciones mecánicas funcionales.
* **Seguridad:** finales de carrera en cada eje para homing.
* **Energía:** compatibilidad con 9 V por limitaciones de fuente.
* **Escalabilidad:** estante parcial → estante completo al reponer piezas.

---

### 2.4 Diagramas de Operación

#### Flujo de operación

```mermaid
sequenceDiagram
    participant Operador
    participant Robot as Robot 3 ejes
    participant Estante

    Operador->>Robot: Inicia ciclo
    Robot->>Robot: Homing de ejes (X, Y, Z)
    Robot->>Estante: Posiciona carro en columna activa
    Robot->>Estante: Deposita o recoge pieza
    Robot->>Punto: Lleva pieza a punto de entrega
    Robot->>Robot: Retorna a origen
    Robot-->>Operador: Ciclo completado
```
---

### 2.5 Retos de Construcción

```mermaid
graph TD
A[Pieza faltante: eje metálico 260 mm] --> B[Solución: reemplazo del tornillo en eje Z por un actuador lineal motorreductor]
A --> C[Consecuencia: eje X no cubre toda la longitud del estante]
C --> D[Impacto: sólo una columna del shelf es funcional]
B --> E[Impacto: cambio de diseño original y posibles errores no previstos en su funcionamiento]
F[Falta de baterías 9 V] --> G[Solución: uso de fuente externa]
G --> H[Impacto: dependencia a la fuente]
```

---

## 3. Configuración Experimental, Resultados y Análisis

### 3.1 Montaje físico

* Ensamble estructural del sistema cartesiano.
* Verificación de homing con finales de carrera.
* Sustitución del tornillo vertical por carril + actuador lineal.
* Validación de movimientos básicos en X, Y y Z.

### 3.2 Programación de rutinas

Se desarrollaron **funciones en ROBO Pro Coding** para inicializar el sistema y controlar los movimientos.

#### Rutinas de referencia (homing)

```python
def reference_m1():
    # Referencia del eje X usando encoder
    TXT_M_M1_encodermotor.move_to(0, 200)
    TXT_M_M1_encodermotor.start_sync()
    TXT_M_M1_encodermotor.wait_for()
    print("Referencia M1 lista")

def reference_m2():
    # Referencia del eje Y hacia el switch I2
    TXT_M_M2_motor.set_speed(150, Motor.CCW)
    TXT_M_M2_motor.start_sync()
    while not TXT_I2_switch.state():
        sleep(0.01)
    TXT_M_M2_motor.stop()
    print("Referencia M2 lista")

def reference_m3():
    # Referencia del eje Z hacia el switch I3
    TXT_M_M3_motor.set_speed(150, Motor.CCW)
    TXT_M_M3_motor.start_sync()
    while not TXT_I3_switch.state():
        sleep(0.01)
    TXT_M_M3_motor.stop()
    print("Referencia M3 lista")

def reference_all():
    # Rutina de referencia global
    display.clear()
    display.draw_text(10, 10, "Haciendo referencia...")
    reference_m1()
    reference_m2()
    reference_m3()
    display.clear()
    display.draw_text(10, 10, "Referencia completa")
    sleep(1)
```

#### Funciones de movimiento

```python
def move_x_to(pos):
    # Movimiento del eje X a posición dada
    TXT_M_M1_encodermotor.move_to(pos, 200)
    TXT_M_M1_encodermotor.start_sync()
    TXT_M_M1_encodermotor.wait_for()

def fork_forward():
    # Avance del carro (eje Y)
    TXT_M_M2_motor.set_speed(150, Motor.CW)
    TXT_M_M2_motor.start_sync()
    while not TXT_I4_switch.state():
        sleep(0.01)
    TXT_M_M2_motor.stop()

def fork_backward():
    # Retroceso del carro (eje Y)
    TXT_M_M2_motor.set_speed(150, Motor.CCW)
    TXT_M_M2_motor.start_sync()
    while not TXT_I2_switch.state():
        sleep(0.01)
    TXT_M_M2_motor.stop()

def fork_up():
    # Elevación del eje Z
    TXT_M_M3_motor.set_speed(150, Motor.CW)
    TXT_M_M3_motor.start_sync()
    t = 0
    while t < 1.5:
        sleep(0.1)
        t += 0.1
    TXT_M_M3_motor.stop()

def fork_down():
    # Descenso del eje Z
    TXT_M_M3_motor.set_speed(150, Motor.CCW)
    TXT_M_M3_motor.start_sync()
    while not TXT_I3_switch.state():
        sleep(0.01)
    TXT_M_M3_motor.stop()
```

#### Diagrama de flujo de software

```mermaid
flowchart TD
    A[Inicio] --> B[Referencia todos los ejes]
    B --> C{Comando recibido}
    C --> D[Almacenar pieza] --> E[Move X + Fork Y + Z up/down]
    C --> F[Recuperar pieza] --> G[Move X + Fork Y + Z up/down]
    E --> H[Retornar a origen]
    G --> H[Retornar a origen]
    H --> C
```

---

### 3.3 Resultados

* Movimientos X, Y, Z estables con alimentación a 9 V.
* Carro deslizable funcional en operaciones de carga y descarga.
* Se comprobó la capacidad mecánica de ejecutar los movimientos necesarios.
* Aún no se validó el código completo → funcionamiento pendiente de depuración.

---

## 4. Avances Constructivos Documentados

Sección reservada para fotos con fecha.

| Fecha      | Imagen                      | Descripción breve                        |
| ---------- | --------------------------- | ---------------------------------------- |
| 2025-08-01 | `media/avance_20250801.jpg` | Ensamble inicial de la base y eje X.     |
| 2025-08-05 | `media/avance_20250805.jpg` | Montaje del carro deslizable (eje Y).    |
| 2025-08-10 | `media/avance_20250810.jpg` | Sustitución del eje 260 mm por actuador. |
| 2025-08-15 | `media/avance_20250815.jpg` | Validación de movimientos con 9 V.       |

---

## 5. Autoevaluación

* **Fortalezas:** ensamble sólido, resolución de problemas prácticos, validación parcial de programación.
* **Debilidades:** operación limitada a 9 V, solo columna 1 activa, código pendiente de prueba.
* **Mejoras:** fuente de alimentación estable, adquisición de repuestos, depuración del software.

---

## 6. Conclusiones y Trabajo Futuro

El prototipo combina **construcción física adaptativa** y **programación en ROBO Pro Coding**.
Se logró un robot funcional en mecánica, con movimientos básicos y rutinas de referencia en software.

Trabajo futuro:

* Completar estante 2×3.
* Depurar y probar el código completo.
* Migrar de baterías a fuente regulada.
* Integrar conectividad IIoT (Modbus/MQTT + dashboard).

---

## 7. Referencias

* Fischertechnik, *Automation Robots – High Bay Storage Rack*.
* Documentación de **ROBO Pro Coding** y **ROBO TX Automation Robots**.
* ISO/IEC/IEEE 29148:2018 — Requirements engineering.

---

## 8. Anexos

* Esquemás: `/docs/`
* Códigos ROBO Pro Coding: `/codes/`
* Avances fotográficos: `/media/avances/`
* Videos de funcionamiento: `/media/videos/`

---
