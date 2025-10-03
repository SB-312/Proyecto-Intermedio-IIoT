# Proyecto Intermedio – IIoT
## PARTES:
1. [PRIMER CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/PRIMER%20CORTE)
2. [SEGUNDO CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/SEGUNDO%20CORTE)

```mermaid

flowchart BT

%% ========= ALIMENTACIÓN (sólo alimenta al NIVEL 1) =========
subgraph PSU["Fuente 9V DC"]
  VCC0["VCC (+9V)"]
  GND0["GND (0V)"]
end

%% ================= NIVEL 3 — Z (arriba) =================
subgraph N3["Nivel 3 — Z (arriba)"]
  direction TB
  Z_REV_NO["Z_REV NO"]:::vcc
  Z_REV_NC["Z_REV NC"]:::gnd

  Z_FWD_NO["Z_FWD NO"]
  Z_FWD_NC["Z_FWD NC"]

  Z_FWD_COM["Z_FWD COM"]
  Z_REV_COM["Z_REV COM"]

  subgraph MZ["Motor Z (DC)"]
    direction TB
    Z_A["Terminal A (Z)"]
    Z_B["Terminal B (Z)"]
  end

  %% Adelante toma del Reversa del MISMO nivel (mini-nodo local)
  Z_FWD_NO --- Z_REV_NO
  Z_FWD_NC --- Z_REV_NC

  %% COM -> motor
  Z_FWD_COM --> Z_A
  Z_REV_COM --> Z_B
end

%% ================= NIVEL 2 — Y (medio) =================
subgraph N2["Nivel 2 — Y (medio)"]
  direction TB
  Y_REV_NO["Y_REV NO"]:::vcc
  Y_REV_NC["Y_REV NC"]:::gnd

  Y_FWD_NO["Y_FWD NO"]
  Y_FWD_NC["Y_FWD NC"]

  Y_FWD_COM["Y_FWD COM"]
  Y_REV_COM["Y_REV COM"]

  subgraph MY["Motor Y (DC)"]
    direction TB
    Y_A["Terminal A (Y)"]
    Y_B["Terminal B (Y)"]
  end

  Y_FWD_NO --- Y_REV_NO
  Y_FWD_NC --- Y_REV_NC

  Y_FWD_COM --> Y_A
  Y_REV_COM --> Y_B
end

%% ================= NIVEL 1 — X (abajo) =================
subgraph N1["Nivel 1 — X (abajo)"]
  direction TB
  X_REV_NO["X_REV NO"]:::vcc
  X_REV_NC["X_REV NC"]:::gnd

  X_FWD_NO["X_FWD NO"]
  X_FWD_NC["X_FWD NC"]

  X_FWD_COM["X_FWD COM"]
  X_REV_COM["X_REV COM"]

  subgraph MX["Motor X (DC)"]
    direction TB
    X_A["Terminal A (X)"]
    X_B["Terminal B (X)"]
  end

  X_FWD_NO --- X_REV_NO
  X_FWD_NC --- X_REV_NC

  X_FWD_COM --> X_A
  X_REV_COM --> X_B
end

%% ========= ALIMENTACIÓN → NIVEL 1 =========
VCC0 --> X_REV_NO
GND0 --> X_REV_NC

%% ========= ELEVADOR VERTICAL (por el lado REVERSA) =========
X_REV_NO --> Y_REV_NO --> Z_REV_NO
X_REV_NC --> Y_REV_NC --> Z_REV_NC

%% ========= ESTILOS OPCIONALES =========
classDef vcc fill:#1a7f37,stroke:#0e4429,color:#ffffff;
classDef gnd fill:#6e7781,stroke:#24292f,color:#ffffff;


```
