# Proyecto Intermedio – IIoT
## PARTES:
1. [PRIMER CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/PRIMER%20CORTE)
2. [SEGUNDO CORTE](https://github.com/SB-312/Proyecto-Intermedio-IIoT/tree/916e029ec4225949f1034e62b44dfbe654ede8cd/SEGUNDO%20CORTE)
flowchart TB
  %% =======================
  %% ALIMENTACIÓN
  %% =======================
  subgraph PSU["Alimentación"]
    PS["Fuente DC 9 V"]
    VCC[/"Riel VCC (+9 V)"/]
    GND[\"Riel GND (0 V)"/]
    PS -- "+" --> VCC
    PS -- "-" --> GND
  end

  %% =======================
  %% NIVEL 3 (ARRIBA) — Z
  %% =======================
  subgraph N3["Nivel 3 — Z (arriba)"]
    subgraph MZ["Motor Z (DC)"]
      MZ_A["Terminal A (Z)"]
      MZ_B["Terminal B (Z)"]
    end

    %% Pulsador Z Adelante
    Z_FWD_NO(("Z_FWD NO"))
    Z_FWD_COM(("Z_FWD COM"))
    Z_FWD_NC(("Z_FWD NC"))

    %% Pulsador Z Reversa
    Z_REV_NO(("Z_REV NO"))
    Z_REV_COM(("Z_REV COM"))
    Z_REV_NC(("Z_REV NC"))

    %% Cableado a rieles
    VCC --> Z_FWD_NO
    GND --> Z_FWD_NC
    VCC --> Z_REV_NO
    GND --> Z_REV_NC

    %% COM a terminales de motor
    Z_FWD_COM --> MZ_A
    Z_REV_COM --> MZ_B
  end

  %% =======================
  %% NIVEL 2 (MEDIO) — Y
  %% =======================
  subgraph N2["Nivel 2 — Y (medio)"]
    subgraph MY["Motor Y (DC)"]
      MY_A["Terminal A (Y)"]
      MY_B["Terminal B (Y)"]
    end

    %% Pulsador Y Adelante
    Y_FWD_NO(("Y_FWD NO"))
    Y_FWD_COM(("Y_FWD COM"))
    Y_FWD_NC(("Y_FWD NC"))

    %% Pulsador Y Reversa
    Y_REV_NO(("Y_REV NO"))
    Y_REV_COM(("Y_REV COM"))
    Y_REV_NC(("Y_REV NC"))

    %% Cableado a rieles
    VCC --> Y_FWD_NO
    GND --> Y_FWD_NC
    VCC --> Y_REV_NO
    GND --> Y_REV_NC

    %% COM a terminales de motor
    Y_FWD_COM --> MY_A
    Y_REV_COM --> MY_B
  end

  %% =======================
  %% NIVEL 1 (ABAJO) — X
  %% =======================
  subgraph N1["Nivel 1 — X (abajo)"]
    subgraph MX["Motor X (DC)"]
      MX_A["Terminal A (X)"]
      MX_B["Terminal B (X)"]
    end

    %% Pulsador X Adelante
    X_FWD_NO(("X_FWD NO"))
    X_FWD_COM(("X_FWD COM"))
    X_FWD_NC(("X_FWD NC"))

    %% Pulsador X Reversa
    X_REV_NO(("X_REV NO"))
    X_REV_COM(("X_REV COM"))
    X_REV_NC(("X_REV NC"))

    %% Cableado a rieles
    VCC --> X_FWD_NO
    GND --> X_FWD_NC
    VCC --> X_REV_NO
    GND --> X_REV_NC

    %% COM a terminales de motor
    X_FWD_COM --> MX_A
    X_REV_COM --> MX_B
  end

  %% =======================
  %% NOTAS
  %% =======================
  %% Al no pulsar: los COM están unidos a NC -> GND.
  %% Al pulsar: los COM conmutan a NO -> VCC.
  %% Recomendación: NO pulsar Adelante y Reversa a la vez en el mismo eje.
