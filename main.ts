let logging = false
input.onButtonPressed(Button.A, function () {
    logging = !(logging)
    if (logging) {
        basic.showIcon(IconNames.Yes)
    } else {
    	
    }
})
loops.everyInterval(500, function () {
    if (logging) {
        datalogger.log(datalogger.createCV("sound level", input.soundLevel()))
    }
})
basic.forever(function () {
    datalogger.setColumnTitles("sound level")
    basic.pause(2000)
    basic.clearScreen()
    serial.writeNumbers([input.soundLevel(), 255])
    basic.showNumber(input.soundLevel())
})
