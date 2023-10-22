import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600)
time.sleep(2)
def wrtToArduino(x):
    arduino.write(bytearray(x, 'ascii'))

wrtToArduino('A')
    