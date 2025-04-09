from machine import pin
import utime

sev_seg = (4, 5, 6, 7)
segments = (9, 10, 11, 12, 14, 15, 16, 17)

patterns = [
    (0, 0, 0, 0, 0, 0, 1, 1),  # 0
    (1, 0, 0, 1, 1, 1, 1, 1),  # 1
    (0, 0, 1, 0, 0, 1, 0, 1),  # 2
    (0, 0, 0, 0, 1, 1, 0, 1),  # 3
    (1, 0, 0, 1, 1, 0, 0, 1),  # 4
    (0, 1, 0, 0, 1, 0, 0, 1),  # 5
    (0, 1, 0, 0, 0, 0, 0, 1),  # 6
    (0, 0, 0, 1, 1, 1, 1, 1),  # 7
    (0, 0, 0, 0, 0, 0, 0, 1),  # 8
    (0, 0, 0, 1, 1, 0, 0, 1)   # 9
]

pins = [Pin(seg, Pin.OUT) for seg in segments]
displays = [Pin(seg, Pin.OUT, value=1) for seg in sev_seg]

def display_digit(display, digit):
    for i in range(4):
        displays[i].value(1)

    pattern = patterns[digit]

    for i in range(8):
        pins[i].value(pattern[i])

    displays[display].value(0)

    utime.sleep_ms(12)

    displays[display].value(1)

while True:
     for i in range(10):
        for j in range(10):
            start = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start) < 1000:
                display_digit(0, i)
                display_digit(1, j)
