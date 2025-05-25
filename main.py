logging = False

def on_button_pressed_a():
    global logging
    logging = not (logging)
    if logging:
        basic.show_icon(IconNames.YES)
    else:
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("sound level", input.sound_level()))
loops.every_interval(500, on_every_interval)

def on_forever():
    datalogger.set_column_titles("sound level")
    basic.pause(2000)
    basic.clear_screen()
    led.plot_bar_graph(input.sound_level(), 255)
basic.forever(on_forever)
