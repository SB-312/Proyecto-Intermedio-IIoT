# Contexto y Requisitos
Este trabajo tiene como objetivo el continuar con la implementacion del proceso descrito en la primera parte de este proyecto, en este caso seria un brazo robot que transportaria cargas desde la bahia al almacen y viceversa. Para ello en este trabajo se hablara de como se conecto el prototipo de manera que es manejable por medio de botones si esta siendo alimentado por nueve voltios y ademas de una simulacion hecha en codesys con el uso de logica ladder la cual representa de manera fiel el funcionamiento mecanico del prototipo en la vida real.

En este caso se debe utilizar un PLC simulado dentro de codesys que utilice una logica ladder la cual tiene que hacer uso de contadores y timers para lograr representar el funcionamiento del prototipo el proceso sera llevado a cabo por medio de interruptores que son accionadas por medio de la HMI, el proceso debe tener luces piloto que muestren al operador como van cambiando los estados del proceso y tambien si hay alguna anomalia durante el mismo. Este HMI debe mostrar animaciones de como se desarrollaria el proceso con el prototipo real mientras el operador manipula los interruptores para ponerlo en funcionamiento o detenerlo si asi lo desea.

## 1) Roles y Contribuciones

| Categoría             | Criterio                                                                 | Responsable |
|-----------------------|---------------------------------------------------------------------------|-------------|
| Gestión de proyecto   | Repositorio Git creado                                                    | Maria Alejandra Cabrera Arauz   |
| Gestión de proyecto   | Estructura de carpetas estandarizada (src/ hmi/ docs/ proto/ video/)      | Maria Alejandra Cabrera Arauz   |
| Gestión de proyecto   | Tablero con Roles y contribuciones por integrante                         | Juan Diego Lemus Rey       |
| Gestión de proyecto   | Visualización del tablero, roles y contribuciones                        | Maria Alejandra Cabrera Arauz   |
| Diseño ingenieril     | Diagrama eléctrico completo (sensores/actuadores ↔ PLC)                  | Juan Diego Lemus Rey       |
| Diseño ingenieril     | Lista de variables (tag list) con atributo y tipo                        | Christian Daniel Morales Jimenez   |
| Diseño ingenieril     | Diagrama de actividades/secuencial del proceso                           | Juan Diego Lemus Rey       |
| Diseño ingenieril     | Ladder conforme IEC 61131-3 con comentarios por red                      | Christian Daniel Morales Jimenez   |
| Diseño ingenieril     | Control por tiempo (temporizadores, estados, transiciones) implementado  | Christian Daniel Morales Jimenez   |
| Validación prototipo  | Diseño de checklist 9V                                                   | Juan Diego Lemus Rey       |
| Validación simulación | Demostración HMI en CODESYS (start/stop, E-Stop, pilotos, estados)       | Christian Daniel Morales Jimenez   |
| HMI (ISA-101)         | Animación simulación 3D                                                  | Juan Diego Lemus Rey       |
| HMI (ISA-101)         | Pantalla principal (estados)                                             | Christian Daniel Morales Jimenez   |
| HMI (Comunic.)        | Guía de 1 página para el operador                                        | Maria Alejandra Cabrera Arauz   |
| Wiki técnica          | Sección Contexto y requisitos (cita Enunciado)                           | Christian Daniel Morales Jimenez   |
| Wiki técnica          | Diagrama(s), criterios, restricciones, estándares aplicados              | Juan Diego Lemus Rey       |
| Wiki técnica          | Arquitectura CODESYS, mapeo de direcciones, Ladder comentado             | Christian Daniel Morales Jimenez   |
| Wiki técnica          | Plan de pruebas, resultados, evidencias (sim y prototipo)                | Maria Alejandra Cabrera Arauz   |
| Wiki técnica          | Declaración del uso de IA y fuentes bibliográficas                       | Maria Alejandra Cabrera Arauz   |
| Video (≤10 min)       | Demostración y explicación clara (sim + prototipo + E-Stop + anomalía)   | Todos       |


## 2) Diagrama de actividades

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

## 3) Diagrama Eléctrico
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
## 4) Diagrama de usabilidad

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

| **Nombre**      | **Tipo de dato** | **Función (I/O/Interno/Timer/Contador)** | **Descripción** |
|-----------------|------------------|------------------------------------------|-----------------|
| **Movement_X**  | INT              | Interno                                  | Posición actual del eje X (0–176). |
| **Movement_Y**  | INT              | Interno                                  | Posición actual del eje Y (0–176). |
| **Movement_Z**  | INT              | Interno                                  | Posición actual del eje Z (0–176). |
| **CountUp_x**   | INT              | Interno                                  | Conteo de incrementos en eje X. |
| **CountD_x**    | INT              | Interno                                  | Conteo de decrementos en eje X. |
| **CountUp_y**   | INT              | Interno                                  | Conteo de incrementos en eje Y. |
| **CountD_y**    | INT              | Interno                                  | Conteo de decrementos en eje Y. |
| **CountUp_z**   | INT              | Interno                                  | Conteo de incrementos en eje Z. |
| **CountD_z**    | INT              | Interno                                  | Conteo de decrementos en eje Z. |
| **Flanco_ax**   | BOOL             | Interno (Relay)                          | Flanco de avance en eje X (detector de pulso). |
| **Flanco_bx**   | BOOL             | Interno (Relay)                          | Flanco de retroceso en eje X. |
| **Flanco_ay**   | BOOL             | Interno (Relay)                          | Flanco de avance en eje Y. |
| **Flanco_by**   | BOOL             | Interno (Relay)                          | Flanco de retroceso en eje Y. |
| **Flanco_az**   | BOOL             | Interno (Relay)                          | Flanco de avance en eje Z. |
| **Flanco_bz**   | BOOL             | Interno (Relay)                          | Flanco de retroceso en eje Z. |
| **Power_light** | BOOL             | Salida                                   | Indicador luminoso de encendido del sistema. |
| **Power_on**    | BOOL             | Entrada                                  | Interruptor general de encendido. |
| **Error**       | BOOL             | Salida                                   | Señal de error general (colisión o doble orden). |
| **Advance_x**   | BOOL             | Entrada                                  | Orden de avance en eje X (desde HMI o pulsador). |
| **Advance_y**   | BOOL             | Entrada                                  | Orden de avance en eje Y. |
| **Advance_z**   | BOOL             | Entrada                                  | Orden de avance en eje Z. |
| **Back_x**      | BOOL             | Entrada                                  | Orden de retroceso en eje X. |
| **Back_y**      | BOOL             | Entrada                                  | Orden de retroceso en eje Y. |
| **Back_z**      | BOOL             | Entrada                                  | Orden de retroceso en eje Z. |
| **Stop**        | BOOL             | Entrada                                  | Botón de paro para detener el proceso. |
| **Limit_ax**    | BOOL             | Entrada (Sensor)                         | Sensor de límite superior en eje X. |
| **Limit_bx**    | BOOL             | Entrada (Sensor)                         | Sensor de límite inferior en eje X. |
| **Limit_ay**    | BOOL             | Entrada (Sensor)                         | Sensor de límite superior en eje Y. |
| **Limit_by**    | BOOL             | Entrada (Sensor)                         | Sensor de límite inferior en eje Y. |
| **Limit_az**    | BOOL             | Entrada (Sensor)                         | Sensor de límite superior en eje Z. |
| **Limit_bz**    | BOOL             | Entrada (Sensor)                         | Sensor de límite inferior en eje Z. |
| **Lamp_ax**     | BOOL             | Salida                                   | Lámpara de estado avance eje X. |
| **Lamp_bx**     | BOOL             | Salida                                   | Lámpara de estado retroceso eje X. |
| **Lamp_ay**     | BOOL             | Salida                                   | Lámpara de estado avance eje Y. |
| **Lamp_by**     | BOOL             | Salida                                   | Lámpara de estado retroceso eje Y. |
| **Lamp_az**     | BOOL             | Salida                                   | Lámpara de estado avance eje Z. |
| **Lamp_bz**     | BOOL             | Salida                                   | Lámpara de estado retroceso eje Z. |
| **Ton_ax**      | TON              | Timer                                    | Temporizador para avance eje X. |
| **Ton_bx**      | TON              | Timer                                    | Temporizador para retroceso eje X. |
| **Ton_ay**      | TON              | Timer                                    | Temporizador para avance eje Y. |
| **Ton_by**      | TON              | Timer                                    | Temporizador para retroceso eje Y. |
| **Ton_az**      | TON              | Timer                                    | Temporizador para avance eje Z. |
| **Ton_bz**      | TON              | Timer                                    | Temporizador para retroceso eje Z. |
| **Cont_ax**     | CTU              | Contador                                 | Contador de pasos avance eje X. |
| **Cont_bx**     | CTU              | Contador                                 | Contador de pasos retroceso eje X. |
| **Cont_ay**     | CTU              | Contador                                 | Contador de pasos avance eje Y. |
| **Cont_by**     | CTU              | Contador                                 | Contador de pasos retroceso eje Y. |
| **Cont_az**     | CTU              | Contador                                 | Contador de pasos avance eje Z. |
| **Cont_bz**     | CTU              | Contador                                 | Contador de pasos retroceso eje Z. |
| **Time_ax**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para avance eje X. |
| **Time_bx**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para retroceso eje X. |
| **Time_ay**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para avance eje Y. |
| **Time_by**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para retroceso eje Y. |
| **Time_az**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para avance eje Z. |
| **Time_bz**     | TIME             | Interno (Tiempo)                         | Tiempo configurado para retroceso eje Z. |

# Logica ladder

## Funcion de encendido

<img width="404" height="66" alt="image" src="https://github.com/user-attachments/assets/b8270efd-1ef2-42d8-b7b5-feadf3d7a07d" />

Esta parte de la logica solo se necarga de controlar el estado de la variable "Power_on" y la luz de encendido que depende de esta variable.

## Funciones de movimiento
## Funciones de avance

<img width="614" height="109" alt="image" src="https://github.com/user-attachments/assets/b62f2316-fb8c-4e2d-bf00-5fbf40972659" />

Esta función consta de un AND de 5 entradas, siendo estas "Power_on" (encendido), la variable de avance en este caso como en el ejemplo es el eje x "Advance_x", "Flanco_ax" la cual depende de la salida del timer esto se hizo con el proposito de que se de flanco a si mismo para crear una animacion fluida, "Error" la cual en caso de que haya una anomalia en el proceso detiene el movimiento y finalmente "Limit_ax" la cual es usada en este ejemplo para validar los limites del movimiento hacia adelante en eje x.

Despues de que la salida del AND sea positva le da flanco al timer quien aparte de controlar la variable "Flanco_ax" en este caso tambien hace que el contador "Cont_ax" aumente y se registre su valor en la variable INT "CountUp_x" la cual se utilizara para determinar en que posicion deberia estar la animacion a lo largo del eje x. Esto funciona de manera identica para el resto de ejes pero con sus respectivas variables.

## Funciones de retroceso

<img width="606" height="111" alt="image" src="https://github.com/user-attachments/assets/4b5cf187-d86f-4fab-800c-d67594f1925f" />

Esta funcion consta de un AND de 5 entradas, siendo estas "Power_on" (encendido), la variable de avance en este caso como en el ejemplo es el eje y "Back_y", "Flanco_by" la cual depende de la salida del timer esto se hizo con el proposito de que se de flanco a si mismo para crear una animacion fluida, "Error" la cual en caso de que haya una anomalia en el proceso detiene el movimiento y finalmente "Limit_bx" la cual es usada en este ejemplo para validar los limites del movimiento hacia atras en eje y.

Despues de que la salida del AND sea positva le da flanco al timer quien aparte de controlar la variable "Flanco_by" en este caso tambien hace que el contador "Cont_by" aumente y se registre su valor en la variable INT "CountD_y" la cual se utilizara para determinar en que posicion deberia estar la animacion a lo largo del eje y. Esto funciona de manera identica para el resto de ejes pero con sus respectivas variables.

## Calculo de posición

<img width="265" height="110" alt="image" src="https://github.com/user-attachments/assets/9cf8ec72-557a-4941-bd3e-f2aba76381d2" />

En el ejmplo se esta claculando la posicion a lo largo del eje z de la animacion con el modulo resta, en este caso siempre calcula valores entre -1 y 177 ya que el eje mide 176, pra eso utiliza las variables "CountUp_z" y "CountD_z" y las resta en ese orden para darle valor a la variable de control "Movement_Z" la cual controla el movimiento de la animacion en el eje z. Esto funciona de manera identica para el resto de ejes pero con sus respectivas variables.

##  Limites
### Limites inferiores
<img width="466" height="114" alt="image" src="https://github.com/user-attachments/assets/2c8d084a-c69f-4129-86bc-1df3718d201d" />

Se compra la variable "Movement_X" para que no se menor a 0, si esta adquiere un valor inferior automaticamente detendra el movimiento hacia atras del eje x. Esto funciona de manera identica para el resto de ejes pero con sus respectivas variables.
### Limites superiores
<img width="464" height="114" alt="image" src="https://github.com/user-attachments/assets/fbff50f4-9970-41b3-b24b-5f0291179889" />

Se compra la variable "Movement_X" para que no se mayor a 176, si esta adquiere un valor superior automaticamente detendra el movimiento hacia adelante del eje x. Esto funciona de manera identica para el resto de ejes pero con sus respectivas variables.
## Funcion de error

<img width="461" height="155" alt="image" src="https://github.com/user-attachments/assets/f7ab2f34-a4b9-4834-8535-025420beb0ae" />

Esta funcion se encarga de disparar la alarma de error la cual detendra todos los movimientos que se esten ejcutando en el momento y ademas encendera la luz correspondiente en el HMI. La manera de activar es hacer ambos movimientos (avanzar y retroceder) de manera simultanea en el mismo eje, para lograrlo se pusieron ambas variables de cada eje en un AND de dos entradas y cada uno de eso AND a un OR de tres entradas ya que son tres ejes para que detenga el proceso sin importar en que eje se de el error.

## Funcion de parada

<img width="399" height="69" alt="image" src="https://github.com/user-attachments/assets/68635033-1bc2-4e4c-bcea-7755cac9523e" />

Esta funcion depende de un boton en el HMI y lo que hace es apagar el proceso para detener todos los movimientos en cualquier momento.

## Funciones de indicadores visuales

<img width="485" height="231" alt="image" src="https://github.com/user-attachments/assets/ff8d78d9-9dd9-4bd5-b1ee-7fbfacb8a0da" />

Cada una de estas funciones es un AND de 4 entradas las cuales serian las mismas que las funciones de movimiento a excepcion del flanco de su timer correspondiente, esto con el proposito de encender la luz que indica su movimiento correspondiente de manera continua (cosa que con el flanco no sucede) y poder dar una mejor retroalimentacion del proceso al operador por medio del HMI.

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
| Stop          | %IX0.7        | GPIO 12       | Botón de paro para detener el proceso |

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

# Plan de Pruebas

El plan de pruebas contempla en primer lugar la verificación del funcionamiento de los botones en los ejes X, Y y Z, asegurando que los comandos de avance y retroceso respondan de forma inmediata, sin bloqueos y dentro de los límites establecidos. En esta fase también se valida que no se activen de manera simultánea las dos direcciones opuestas de un mismo eje, lo cual podría generar errores lógicos o fallas eléctricas. Paralelamente, se supervisa la alimentación eléctrica para confirmar que se mantenga en 9V constantes y que no se produzcan sobrecargas ni riesgos de cortocircuito durante el uso.

En una segunda etapa se revisa el correcto funcionamiento de los indicadores luminosos, confirmando que cada color corresponda al estado real del sistema: verde para avanzar, naranja para retroceder, y rojo para errores. De manera complementaria, en el entorno de simulación (HMI/CODESYS) se verifica que los movimientos se mantengan dentro de los límites configurados y que la representación gráfica sea coherente con la lógica implementada, permitiendo detectar anomalías antes de llevar las pruebas al prototipo físico.

# Uso de IA y referencias

## Promts de IA
### 1) Uso para realizar Manual de Usuario
<img width="682" height="670" alt="image" src="https://github.com/user-attachments/assets/64ca7c31-7210-4244-9844-a05887a29f59" />

### 2) Uso para realizar Plan de Pruebas
<img width="680" height="577" alt="image" src="https://github.com/user-attachments/assets/43abaef1-0dc2-4172-b78c-b284500408d6" />

## Referencias

