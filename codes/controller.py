import fischertechnik.factories as txt_factory

txt_factory.init()
txt_factory.init_input_factory()
txt_factory.init_motor_factory()

TXT_M = txt_factory.controller_factory.create_graphical_controller()
TXT_M_I1_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 1)
TXT_M_I2_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 2)
TXT_M_I3_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 3)
TXT_M_I4_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 4)
TXT_M_I5_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 5)
TXT_M_I6_mini_switch = txt_factory.input_factory.create_mini_switch(TXT_M, 6)
TXT_M_M1_encodermotor = txt_factory.motor_factory.create_encodermotor(TXT_M, 1)
TXT_M_M2_motor = txt_factory.motor_factory.create_motor(TXT_M, 2)
TXT_M_M3_motor = txt_factory.motor_factory.create_motor(TXT_M, 3)

txt_factory.initialized()