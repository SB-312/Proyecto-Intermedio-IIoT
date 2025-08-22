from fischertechnik.controller.Motor import Motor
from lib.controller import *
from lib.graphics import display
from time import sleep
import sys   # para salir del programa al presionar I6

# ------------------------------
# FUNCIONES DE CONTROL
# ------------------------------

def check_stop():
    """Verifica si se presionó I6 (finalizar)"""
    if TXT_I6_switch.state():  # Botón STOP
        TXT_M_M1_encodermotor.stop()
        TXT_M_M2_motor.stop()
        TXT_M_M3_motor.stop()
        display.clear()
        display.draw_text(10, 10, "Programa finalizado")
        sleep(1)
        sys.exit()   # salir del programa por completo

def wait_for_start():
    """Espera hasta que se presione I5 para iniciar"""
    display.clear()
    display.draw_text(10, 10, "Presione I5 para iniciar")
    while not TXT_I5_switch.state():
        check_stop()
        sleep(0.1)
    display.clear()
    display.draw_text(10, 10, "Iniciando...")
    sleep(1)

# ------------------------------
# FUNCIONES DE REFERENCIA
# ------------------------------

def reference_m1():
    TXT_M_M1_encodermotor.move_to(0, 200)
    TXT_M_M1_encodermotor.start_sync()
    TXT_M_M1_encodermotor.wait_for()
    print("Referencia M1 lista")

def reference_m2():
    TXT_M_M2_motor.set_speed(150, Motor.CCW)
    TXT_M_M2_motor.start_sync()
    while not TXT_I2_switch.state():
        check_stop()
        sleep(0.01)
    TXT_M_M2_motor.stop()
    print("Referencia M2 lista")

def reference_m3():
    TXT_M_M3_motor.set_speed(150, Motor.CCW)
    TXT_M_M3_motor.start_sync()
    while not TXT_I3_switch.state():
        check_stop()
        sleep(0.01)
    TXT_M_M3_motor.stop()
    print("Referencia M3 lista")

def reference_all():
    display.clear()
    display.draw_text(10, 10, "Haciendo referencia...")
    reference_m1()
    reference_m2()
    reference_m3()
    display.clear()
    display.draw_text(10, 10, "Referencia completa")
    sleep(1)

# ------------------------------
# FUNCIONES DE MOVIMIENTO
# ------------------------------

def move_x_to(pos):
    TXT_M_M1_encodermotor.move_to(pos, 200) #Posicion y velocidad
    TXT_M_M1_encodermotor.start_sync()
    TXT_M_M1_encodermotor.wait_for()

def fork_forward():
    TXT_M_M2_motor.set_speed(150, Motor.CW) #Velocidad y direccion
    TXT_M_M2_motor.start_sync()
    while not TXT_I4_switch.state():
        check_stop()
        sleep(0.01)
    TXT_M_M2_motor.stop()

def fork_backward():
    TXT_M_M2_motor.set_speed(150, Motor.CCW) #Velocidad y direccion
    TXT_M_M2_motor.start_sync()
    while not TXT_I2_switch.state():
        check_stop()
        sleep(0.01)
    TXT_M_M2_motor.stop()

def fork_up():
    TXT_M_M3_motor.set_speed(150, Motor.CW) #Velocidad y direccion
    TXT_M_M3_motor.start_sync()
    t = 0
    while t < 1.5:
        check_stop()
        sleep(0.1)
        t += 0.1
    TXT_M_M3_motor.stop()

def fork_down():
    TXT_M_M3_motor.set_speed(150, Motor.CCW) #Velocidad y direccion
    TXT_M_M3_motor.start_sync()
    while not TXT_I3_switch.state():
        check_stop()
        sleep(0.01)
    TXT_M_M3_motor.stop()

# ------------------------------
# LOOP PRINCIPAL
# ------------------------------

def setup():
    wait_for_start()   # esperar botón I5
    reference_all()
    display.clear()
    display.draw_text(10, 10, "Sistema listo")
    sleep(1)

def loop():
    # --- Tarea 1 ---
    move_x_to(0)         
    fork_forward()       
    fork_up()            
    fork_backward()      
    sleep(1)

    move_x_to(4000)      
    fork_forward()       
    fork_down()          
    fork_backward()      
    sleep(2)

    # --- Tarea 2 ---
    move_x_to(8000)      
    fork_forward()
    fork_up()
    fork_backward()
    sleep(1)

    move_x_to(0)
    fork_forward()
    fork_down()
    fork_backward()
    sleep(2)

# ------------------------------
# INICIO
# ------------------------------

setup()

while True:
    check_stop()
    loop()