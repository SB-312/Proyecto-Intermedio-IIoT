# Proyecto Intermedio – IIoT
## PARTES:
1. [PRIMER CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/PRIMER%20CORTE)
2. [SEGUNDO CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/SEGUNDO%20CORTE)

```mermaid
flowchart BT
  %% Layout bottom→top (PSU abajo, luego Nivel 1, Nivel 2, Nivel 3)

  %% ========= ALIMENTACIÓN (solo alimenta al NIVEL 1) =========
  subgraph PSU["Fuente 9 V DC"]
    VCC0[+" VCC (+9 V)"]
    GND0[-" GND (0 V)"]
  end

  %% ================= NIVEL 1 — X (abajo) =================
  subgraph N1["Nivel 1 — X (abajo)"]
  direction TB
    %% Nodo local (lado REV) -> sirve como "mini-riel" del nivel
    X_REV_NO(("X_REV NO")):::vccnode
    X_REV_NC(("X_REV NC")):::gndnode

    %% Adelante toma del Reversa (mismo nivel) para no subir cables extra
    X_FWD_NO(("X_FWD NO"))
    X_FWD_NC(("X_FWD NC"))

    %% COM verticales -> a motor
    X_FWD_COM(("X_FWD COM"))
    X_REV_COM(("X_REV COM"))

    %% Motor X (vertical para evitar cruces)
    subgraph MX["Motor X (DC)"]
    direction TB
      X_A["Terminal A (X)"]
      X_B["Terminal B (X)"]
    end

    %% Conexiones locales del nivel
    X_FWD_NO --- X_REV_NO
    X_FWD_NC --- X_REV_NC

    %% COM -> motor
    X_FWD_COM --> X_A
    X_REV_COM --> X_B
  end

  %% ================= NIVEL 2 — Y (medio) =================
  subgraph N2["Nivel 2 — Y (medio)"]
  direction TB
    Y_REV_NO(("Y_REV NO")):::vccnode
    Y_REV_NC(("Y_REV NC")):::gndnode

    Y_FWD_NO(("Y_FWD NO"))
    Y_FWD_NC(("Y_FWD NC"))

    Y_FWD_COM(("Y_FWD COM"))
    Y_REV_COM(("Y_REV COM"))

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

  %% ================= NIVEL 3 — Z (arriba) =================
  subgraph N3["Nivel 3 — Z (arriba)"]
  direction TB
    Z_REV_NO(("Z_REV NO")):::vccnode
    Z_REV_NC(("Z_REV NC")):::gndnode

    Z_FWD_NO(("Z_FWD NO"))
    Z_FWD_NC(("Z_FWD NC"))

    Z_FWD_COM(("Z_FWD COM"))
    Z_REV_COM(("Z_REV COM"))

    subgraph MZ["Motor Z (DC)"]
    direction TB
      Z_A["Terminal A (Z)"]
      Z_B["Terminal B (Z)"]
    end

    Z_FWD_NO --- Z_REV_NO
    Z_FWD_NC --- Z_REV_NC

    Z_FWD_COM --> Z_A
    Z_REV_COM --> Z_B
  end

  %% ========= ALIMENTACIÓN → NIVEL 1 (único contacto con la fuente) =========
  VCC0 --> X_REV_NO
  GND0 --> X_REV_NC

  %% ========= ELEVADOR DE VCC/GND POR EL LADO REVERSA (en columna) =========
  X_REV_NO --> Y_REV_NO --> Z_REV_NO
  X_REV_NC --> Y_REV_NC --> Z_REV_NC

  %% ========= Estilos mínimos para distinguir VCC/GND locales =========
  classDef vccnode fill:#1b6,stroke:#0a4,color:#fff,stroke-width:1px;
  classDef gndnode fill:#666,stroke:#333,color:#fff,stroke-width:1px;

```
