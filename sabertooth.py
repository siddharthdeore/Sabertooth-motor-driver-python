import time
import serial
import sys
# interpolates the variable from input to output range
def lerp(x, min_in, max_in, min_out, max_out):
    return int(min_out + (x - min_in) * (max_out-min_out)/(max_in-min_in))

# Rotates First Motor conected to M1A M1B of Sabertooth 2X25 or 2X60 Motor Driver


def motorA(speed):
    output = lerp(speed, -100, 100, 0, 127)
    Sabertooth_Serial.write(output.to_bytes(1, 'little'))

# Rotates Second Motor conected to M2A M2B of Sabertooth 2X25 or 2X60 Motor Driver


def motorB(speed):
    output = lerp(speed, -100, 100, 128, 255)
    Sabertooth_Serial.write(output.to_bytes(1, 'little'))


try:
    port_name = "/dev/ttyTHS1"
    baud_rate = 9600

    # Open Serial Port
    Sabertooth_Serial = serial.Serial(
        port=port_name, # SERIAL PORT on SBC 
        baudrate = baud_rate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    
    i=0
    j=0
    while 1:
        motorA(i)
        motorB(j)
        time.sleep(0.1)
        i += 1
        j -= 1
        
        if (i > 100 or j >100):
            i,j=j,i

    # Close Serial Port            
    Sabertooth_Serial.close() 

except serial.SerialException as e:
    print(f"Error writing to serial port: {e}")
