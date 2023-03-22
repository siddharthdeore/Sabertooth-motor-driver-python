import time

from sabertooth_serial import SabertoothSerial

if __name__ == "__main__":
    port_name = "/dev/ttyUSB0"
    baud_rate = 9600
    motor_driver = SabertoothSerial(port_name,baud_rate)
    
    for i in range(-100, 101):        
        motor_driver.motorA(i)
        motor_driver.motorB(i)
        time.sleep(0.1)