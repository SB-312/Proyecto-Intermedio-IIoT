# Contexto y Requisitos
Este trabajo tiene como objetivo el continuar con la implementacion del proceso descrito en la primera parte de este proyecto, en este caso seria un brazo robot que transportaria cargas desde la bahia al almacen y viceversa. Para ello en este trabajo se hablara de como se conecto el prototipo de manera que es manejable por medio de botones si esta siendo alimentado por nueve voltios y ademas de una simulacion hecha en codesys con el uso de logica ladder la cual representa de manera fiel el funcionamiento mecanico del prototipo en la vida real.
En este caso se debe utilizar un PLC simulado dentro de codesys que utilice una logica ladder la cual tiene que hacer uso de contadores y timers para lograr representar el funcionamiento del prototipo el proceso sera llevado a cabo por medio de interruptores que son accionadas por medio de la HMI, el proceso debe tener luces piloto que muestren al operador como van cambiando los estados del proceso y tambien si hay alguna anomalia durante el mismo. Este HMI debe mostrar animaciones de como se desarrollaria el proceso con el prototipo real mientras el operador manipula los interruptores para ponerlo en funcionamiento o detenerlo si asi lo desea.

## 1) Diagrama de actividades

```mermaid
flowchart LR
  %% Role styles
  classDef Lemus fill:#e6f4ea,stroke:#1a7f37,color:#0b3d2e;
  classDef Christian fill:#e7f0fa,stroke:#1b4b91,color:#0b2a66;
  classDef Alejandra fill:#fff1f0,stroke:#b3261e,color:#5f1410;
  classDef Todos fill:#f5f5f5,stroke:#6e7781,color:#24292f;
  classDef Critico stroke:#b3261e,stroke-width:2px;

  %% Gestión
  G1[Repo Git and Wiki enabled]:::Alejandra --> 
  G2[Standard folders ready]:::Alejandra -->
  G3[Kanban with roles and contributions]:::Lemus -->
  G4[Board visible with issues assigned]:::Alejandra

  %% Diseño y validación temprana
  D1[HMI basic animation for sanity check]:::Lemus --> 
  D2[Physical scheme of SPDT pushbuttons X Y Z]:::Lemus -->
  D3[Tag list with attribute and type]:::Christian

  %% Implementación PLC y demo HMI
  P1[Ladder IEC 61131-3 with comments]:::Christian -->
  P2[Time control and counters]:::Christian -->
  P3[HMI demo in CODESYS start stop pilots states]:::Lemus

  %% Cableado y prueba 9V
  V1[Checklist 9V draft and review]:::Lemus -->
  V2[Run 9V test and record evidence]:::Todos -->
  V3{Expected behavior?}
  V3 -->|Yes| V4[Consolidate results and screenshots]:::Alejandra
  V3 -->|No| F1[Diagnose and correct]:::Todos

  %% Incidencia mecánica Z
  F1 --> Z1[Issue: Z gear does not mesh but motor activates]:::Todos -->
  Z2[Register issue in Wiki with short clip]:::Alejandra -->
  Z3[Decision: operate Z with low load or document limitation]:::Todos

  %% Documentación y video
  W1[Implementation in Wiki: architecture and IO map]:::Christian -->
  W2[Design in Wiki: electrical diagram and standards ISA-101 and IEC 61131-3]:::Lemus -->
  W3[Test plan results and evidence]:::Alejandra -->
  W4[One page operator guide]:::Alejandra -->
  W5[Declaration of AI use and sources]:::Alejandra -->
  VID[Video <= 10 min: sim plus prototype plus E-Stop plus fault]:::Todos -->
  ENT[Submit links in Teams and zip package]:::Alejandra

  %% Mark critical path steps
  class VID,ENT Critico;


```
---

## 2) Diagrama Eléctrico
```mermaid

flowchart BT

%% === PSU (feeds Level X only) ===
subgraph PSU["9V DC supply"]
  VCC0["VCC (+9V)"]
  GND0["GND (0V)"]
end

%% === LEVEL 3 — Z (top) ===
subgraph L3["Shelf level 3 — Z (top)"]
  direction LR
  subgraph ZREV["REV rail (Z)"]
    direction TB
    Z_REV_COM["Z_REV COM"]
    Z_REV_NO["Z_REV NO"]
    Z_REV_NC["Z_REV NC"]
  end
  subgraph ZFWD["FWD rail (Z)"]
    direction TB
    Z_FWD_COM["Z_FWD COM"]
    Z_FWD_NO["Z_FWD NO"]
    Z_FWD_NC["Z_FWD NC"]
  end
  subgraph ZM["Motor Z (DC)"]
    direction TB
    Z_A["Terminal A (Z)"]
    Z_B["Terminal B (Z)"]
  end
  %% FWD takes from REV at same level
  Z_FWD_NO --- Z_REV_NO
  Z_FWD_NC --- Z_REV_NC
  %% COMs to motor
  Z_FWD_COM --> Z_A
  Z_REV_COM --> Z_B
end

%% === LEVEL 2 — Y (middle) ===
subgraph L2["Shelf level 2 — Y (middle)"]
  direction LR
  subgraph YREV["REV rail (Y)"]
    direction TB
    Y_REV_COM["Y_REV COM"]
    Y_REV_NO["Y_REV NO"]
    Y_REV_NC["Y_REV NC"]
  end
  subgraph YFWD["FWD rail (Y)"]
    direction TB
    Y_FWD_COM["Y_FWD COM"]
    Y_FWD_NO["Y_FWD NO"]
    Y_FWD_NC["Y_FWD NC"]
  end
  subgraph YM["Motor Y (DC)"]
    direction TB
    Y_A["Terminal A (Y)"]
    Y_B["Terminal B (Y)"]
  end
  Y_FWD_NO --- Y_REV_NO
  Y_FWD_NC --- Y_REV_NC
  Y_FWD_COM --> Y_A
  Y_REV_COM --> Y_B
end

%% === LEVEL 1 — X (bottom) ===
subgraph L1["Shelf level 1 — X (bottom)"]
  direction LR
  subgraph XREV["REV rail (X)"]
    direction TB
    X_REV_COM["X_REV COM"]
    X_REV_NO["X_REV NO"]
    X_REV_NC["X_REV NC"]
  end
  subgraph XFWD["FWD rail (X)"]
    direction TB
    X_FWD_COM["X_FWD COM"]
    X_FWD_NO["X_FWD NO"]
    X_FWD_NC["X_FWD NC"]
  end
  subgraph XM["Motor X (DC)"]
    direction TB
    X_A["Terminal A (X)"]
    X_B["Terminal B (X)"]
  end
  X_FWD_NO --- X_REV_NO
  X_FWD_NC --- X_REV_NC
  X_FWD_COM --> X_A
  X_REV_COM --> X_B
end

%% === PSU → Level X only; then VCC/GND climb on the REV side ===
VCC0 --> X_FWD_NO
GND0 --> X_FWD_NC
X_FWD_NO --> Y_FWD_NO --> Z_FWD_NO
X_FWD_NC --> Y_FWD_NC --> Z_FWD_NC

%% === Optional node styling for quick orientation ===
classDef vcc fill:#1a7f37,stroke:#0e4429,color:#fff;
classDef gnd fill:#6e7781,stroke:#24292f,color:#fff;
class X_REV_NO,Y_REV_NO,Z_REV_NO,X_FWD_NO,Y_FWD_NO,Z_FWD_NO vcc;
class X_REV_NC,Y_REV_NC,Z_REV_NC,X_FWD_NC,Y_FWD_NC,Z_FWD_NC gnd;

```

---
## 3) Diagrama de usabilidad

```mermaid
flowchart TD
  A[Power on 9V supply] --> B{Select level: X, Y or Z}
  B -->|X| X0[Pushbuttons X]
  B -->|Y| Y0[Pushbuttons Y]
  B -->|Z| Z0[Pushbuttons Z]

  %% ---- X ----
  X0 --> X1{What do you press on X?}
  X1 -->|FWD| X2[VCC to COM_FWD_X and GND to COM_REV_X]
  X1 -->|REV| X3[GND to COM_FWD_X and VCC to COM_REV_X]
  X1 -->|None| X4[GND and GND at motor X - idle]
  X1 -->|Both| X5[VCC and VCC at motor X - warning]
  X2 --> X6[Motor X spins direction 1]
  X3 --> X7[Motor X spins direction 2]

  %% ---- Y ----
  Y0 --> Y1{What do you press on Y?}
  Y1 -->|FWD| Y2[VCC to COM_FWD_Y and GND to COM_REV_Y]
  Y1 -->|REV| Y3[GND to COM_FWD_Y and VCC to COM_REV_Y]
  Y1 -->|None| Y4[GND and GND at motor Y - idle]
  Y1 -->|Both| Y5[VCC and VCC at motor Y - warning]
  Y2 --> Y6[Motor Y spins direction 1]
  Y3 --> Y7[Motor Y spins direction 2]

  %% ---- Z ----
  Z0 --> Z1{What do you press on Z?}
  Z1 -->|FWD| Z2[VCC to COM_FWD_Z and GND to COM_REV_Z]
  Z1 -->|REV| Z3[GND to COM_FWD_Z and VCC to COM_REV_Z]
  Z1 -->|None| Z4[GND and GND at motor Z - idle]
  Z1 -->|Both| Z5[VCC and VCC at motor Z - warning]
  Z2 --> Z6[Motor Z spins direction 1]
  Z3 --> Z7[Motor Z spins direction 2]


  %% ---- Styling for warnings ----
  classDef warn fill:#fff3cd,stroke:#b68b00,color:#333;
  class X5,Y5,Z5 warn;
```
---

# Documentación de variables en codesys

| **Nombre**      | **Tipo** | **Descripción** |
|-----------------|----------|-----------------|
| Movement_X      | INT      | Posición actual del eje X (0–176). |
| Movement_Y      | INT      | Posición actual del eje Y (0–176). |
| Movement_Z      | INT      | Posición actual del eje Z (0–176). |
| CountUp_x       | INT      | Conteo de incrementos en eje X. |
| CountD_x        | INT      | Conteo de decrementos en eje X. |
| CountUp_y       | INT      | Conteo de incrementos en eje Y. |
| CountD_y        | INT      | Conteo de decrementos en eje Y. |
| CountUp_z       | INT      | Conteo de incrementos en eje Z. |
| CountD_z        | INT      | Conteo de decrementos en eje Z. |
| Flanco_ax       | BOOL     | Flanco de avance en eje X (detector de pulso). |
| Flanco_bx       | BOOL     | Flanco de retroceso en eje X. |
| Flanco_ay       | BOOL     | Flanco de avance en eje Y. |
| Flanco_by       | BOOL     | Flanco de retroceso en eje Y. |
| Flanco_az       | BOOL     | Flanco de avance en eje Z. |
| Flanco_bz       | BOOL     | Flanco de retroceso en eje Z. |
| Power_light     | BOOL     | Indicador luminoso de encendido del sistema. |
| Power_on        | BOOL     | Interruptor general de encendido. |
| Error           | BOOL     | Señal de error general (colisión o doble orden). |
| Advance_x       | BOOL     | Orden de avance en eje X (desde HMI o pulsador). |
| Advance_y       | BOOL     | Orden de avance en eje Y. |
| Advance_z       | BOOL     | Orden de avance en eje Z. |
| Back_x          | BOOL     | Orden de retroceso en eje X. |
| Back_y          | BOOL     | Orden de retroceso en eje Y. |
| Back_z          | BOOL     | Orden de retroceso en eje Z. |
| Limit_ax        | BOOL     | Sensor de límite superior en eje X. |
| Limit_bx        | BOOL     | Sensor de límite inferior en eje X. |
| Limit_ay        | BOOL     | Sensor de límite superior en eje Y. |
| Limit_by        | BOOL     | Sensor de límite inferior en eje Y. |
| Limit_az        | BOOL     | Sensor de límite superior en eje Z. |
| Limit_bz        | BOOL     | Sensor de límite inferior en eje Z. |
| Lamp_ax         | BOOL     | Lámpara de estado avance eje X. |
| Lamp_bx         | BOOL     | Lámpara de estado retroceso eje X. |
| Lamp_ay         | BOOL     | Lámpara de estado avance eje Y. |
| Lamp_by         | BOOL     | Lámpara de estado retroceso eje Y. |
| Lamp_az         | BOOL     | Lámpara de estado avance eje Z. |
| Lamp_bz         | BOOL     | Lámpara de estado retroceso eje Z. |
| Ton_ax          | TON      | Temporizador para avance eje X. |
| Ton_bx          | TON      | Temporizador para retroceso eje X. |
| Ton_ay          | TON      | Temporizador para avance eje Y. |
| Ton_by          | TON      | Temporizador para retroceso eje Y. |
| Ton_az          | TON      | Temporizador para avance eje Z. |
| Ton_bz          | TON      | Temporizador para retroceso eje Z. |
| Cont_ax         | CTU      | Contador de pasos avance eje X. |
| Cont_bx         | CTU      | Contador de pasos retroceso eje X. |
| Cont_ay         | CTU      | Contador de pasos avance eje Y. |
| Cont_by         | CTU      | Contador de pasos retroceso eje Y. |
| Cont_az         | CTU      | Contador de pasos avance eje Z. |
| Cont_bz         | CTU      | Contador de pasos retroceso eje Z. |
| Time_ax         | TIME     | Tiempo configurado para avance eje X. |
| Time_bx         | TIME     | Tiempo configurado para retroceso eje X. |
| Time_ay         | TIME     | Tiempo configurado para avance eje Y. |
| Time_by         | TIME     | Tiempo configurado para retroceso eje Y. |
| Time_az         | TIME     | Tiempo configurado para avance eje Z. |
| Time_bz         | TIME     | Tiempo configurado para retroceso eje Z. |

# Mapeo de salidas y entradas

## Entradas digitales

| **Variable**  | **Dirección** | **Pin ESP32** | **Descripción** |
|---------------|---------------|----------------|-----------------|
| Power_on      | %IX0.0        | GPIO 13       | Botón de encendido general |
| Advance_x     | %IX0.1        | GPIO 14       | Botón avance eje X |
| Back_x        | %IX0.2        | GPIO 27       | Botón retroceso eje X |
| Advance_y     | %IX0.3        | GPIO 26       | Botón avance eje Y |
| Back_y        | %IX0.4        | GPIO 25       | Botón retroceso eje Y |
| Advance_z     | %IX0.5        | GPIO 33       | Botón avance eje Z |
| Back_z        | %IX0.6        | GPIO 32       | Botón retroceso eje Z |

## Salidas digitales

| **Variable**  | **Dirección** | **Pin ESP32** | **Descripción** |
|---------------|---------------|----------------|-----------------|
| Power_light   | %QX0.0        | GPIO 2        | Luz de encendido general |
| Lamp_ax       | %QX0.1        | GPIO 4        | Luz avance eje X |
| Lamp_bx       | %QX0.2        | GPIO 5        | Luz retroceso eje X |
| Lamp_ay       | %QX0.3        | GPIO 18       | Luz avance eje Y |
| Lamp_by       | %QX0.4        | GPIO 19       | Luz retroceso eje Y |
| Lamp_az       | %QX0.5        | GPIO 21       | Luz avance eje Z |
| Lamp_bz       | %QX0.6        | GPIO 22       | Luz retroceso eje Z |
| Error         | %QX0.7        | GPIO 23       | Luz/alarm indicador de error |
