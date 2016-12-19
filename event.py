import uinput
device = uinput.Device([
    uinput.KEY_A
    ])
device.emit_click(uinput.KEY_A)
