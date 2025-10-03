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

