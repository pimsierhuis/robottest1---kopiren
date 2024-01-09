input.onButtonPressed(Button.A, function () {
    moetrijden = 1
    while (moetrijden) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 100)
        neZha.setMotorSpeed(neZha.MotorList.M2, 100)
        basic.pause(50)
        afstandMeten()
        if (afstand < 30) {
            neZha.setMotorSpeed(neZha.MotorList.M1, -100)
            neZha.setMotorSpeed(neZha.MotorList.M2, -100)
            basic.pause(500)
            neZha.setMotorSpeed(neZha.MotorList.M1, 100)
            neZha.setMotorSpeed(neZha.MotorList.M2, -100)
            basic.pause(500)
        }
    }
})
function afstandMeten () {
    afstand = sonar.ping(
    DigitalPin.P16,
    DigitalPin.P15,
    PingUnit.Centimeters
    )
    while (afstand == 0) {
        afstand = sonar.ping(
        DigitalPin.P16,
        DigitalPin.P15,
        PingUnit.Centimeters
        )
    }
    led.plotBarGraph(
    afstand,
    200
    )
    if (afstand < 200) {
        serial.writeNumber(afstand)
    }
}
input.onButtonPressed(Button.B, function () {
    moetrijden = 0
    neZha.setMotorSpeed(neZha.MotorList.M1, 0)
    neZha.setMotorSpeed(neZha.MotorList.M2, 0)
})
let afstand = 0
let moetrijden = 0
moetrijden = 0
basic.forever(function () {
    serial.writeLine("")
})
