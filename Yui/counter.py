from main import create_pixel
import atexit
import time

QUANTITY = 0


def quantity_up():
    global QUANTITY
    QUANTITY += 1
    print(QUANTITY)


try:
    is_on = True
    while is_on:
        time.sleep(60)
        quantity_up()
finally:
    atexit.register(create_pixel(str(QUANTITY)))
