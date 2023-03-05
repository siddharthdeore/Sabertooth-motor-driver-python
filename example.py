import time

from sabertooth_serial import SabertoothSerial

if __name__ == "__main__":
    motor_driver = SabertoothSerial('/dev/ttyAMA0',9600)
    
    for i in range(-100, 101):        
        motor_driver.motorA(i)
        motor_driver.motorB(i)
        time.sleep(0.1)