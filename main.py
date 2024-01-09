def on_button_pressed_a():
    global moetrijden
    moetrijden = 1
    while moetrijden:
        neZha.set_motor_speed(neZha.MotorList.M1, 100)
        neZha.set_motor_speed(neZha.MotorList.M2, 100)
        basic.pause(50)
        afstandMeten()
        if afstand < 30:
            neZha.set_motor_speed(neZha.MotorList.M1, -100)
            neZha.set_motor_speed(neZha.MotorList.M2, -100)
            basic.pause(500)
            neZha.set_motor_speed(neZha.MotorList.M1, 100)
            neZha.set_motor_speed(neZha.MotorList.M2, -100)
            basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def afstandMeten():
    global afstand
    afstand = sonar.ping(DigitalPin.P16, DigitalPin.P15, PingUnit.CENTIMETERS)
    while afstand == 0:
        afstand = sonar.ping(DigitalPin.P16, DigitalPin.P15, PingUnit.CENTIMETERS)
    led.plot_bar_graph(afstand, 200)
    if afstand < 200:
        serial.write_number(afstand)

def on_button_pressed_b():
    global moetrijden
    moetrijden = 0
    neZha.set_motor_speed(neZha.MotorList.M1, 0)
    neZha.set_motor_speed(neZha.MotorList.M2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

afstand = 0
moetrijden = 0
moetrijden = 0

def on_forever():
    serial.write_line("")
basic.forever(on_forever)
