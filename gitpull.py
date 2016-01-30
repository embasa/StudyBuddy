from subprocess import call
import time

while True:
    call(["git","pull"])
    time.sleep(3)

