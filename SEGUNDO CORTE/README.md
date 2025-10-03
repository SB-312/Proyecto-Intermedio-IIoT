## 1) Diagrama de actividades

```mermaid
flowchart LR
  %% ===== Lanes (subgraphs) por responsable =====
  subgraph A [Alejandra]
    A1[Repo and Wiki enabled]
    A2[Standard folders ready]
    A4[Board visible with assigned issues]
    A9[Consolidate results and screenshots]
    A11[Log Z issue in Wiki with clip]
    A12[Test plan results and evidence]
    A13[One page operator guide]
    A14[AI use and sources]
    A16[Submit in Teams repo link video zip]
  end

  subgraph L [Lemus]
    L1[Kanban with roles and contributions]
    L2[HMI basic animation sanity check]
    L3[Physical scheme pushbuttons SPDT X Y Z]
    L5[HMI demo in CODESYS start stop pilots states]
    L7[Checklist 9V draft with AI and review]
    L11[Design in Wiki electrical diagram and standards ISA 101 and IEC 61131 3]
  end

  subgraph C [Christian]
    C1[Tag list with attribute and type]
    C2[Ladder IEC 61131 3 with comments]
    C3[Time control and counters]
    C10[Implementation in Wiki CODESYS architecture and IO map]
  end

  subgraph T [All team]
    T1[9V test and record evidence]
    D1{Expected behavior}
    F1[Diagnose and correct]
    Z2[Decision operate Z with low load or document limitation]
    V1[Video 10 min simulation prototype E Stop fault]
  end

  %% ===== Flujo principal =====
  A1 --> A2 --> L1 --> A4
  A4 --> L2 --> L3 --> C1 --> C2 --> C3 --> L5
  L5 --> L7 --> T1 --> D1
  D1 -- Yes --> A9 --> A11 --> Z2 --> A12 --> A13 --> A14 --> C10 --> L11 --> V1 --> A16
  D1 -- No --> F1 --> T1


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
