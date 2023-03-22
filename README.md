# Sabertooth Motor Driver with Nvidia Jetson TK1
Motor Driver : Sabertooth 2X60 / Sabertooth 2X25 <br>
Motors : Maxon Brushed DC Motor <br>
Tested on Raspberry PI, ODroid XU4, Nvidia Jetson TK1

first install python-serial to your single board computer
```
sudo apt-get install python-serial
```
in your python script import time and serial module

``` python
import time
import serial
``` 
defination of linear interpolation function similler to arduino map()

``` python
def lerp( x, min_in, max_in, min_out, max_out ):
	return min_out + (x - min_in) * (max_out-min_out)/(max_in-min_in)
``` 
Sabertooth motor rotation functions

``` python
#Rotates First Motor conected to M1A M1B of Sabertooth 2X25 or 2X60 Motor Driver
def motorA( speed ):
	output = int(lerp(speed, -100, 100, 0, 127))
	Sabertooth_Serial.write(output.to_bytes(1,'little'))
	
#Rotates Second Motor conected to M2A M2B of Sabertooth 2X25 or 2X60 Motor Driver
def motorB( speed ):
	output = int(lerp(speed, -100, 100, 128, 255))
	Sabertooth_Serial.write(output.to_bytes(1,'little'))
``` 
to send data to sabertooth, open serial port

``` python
try:
	# Open Serial Port
	Sabertooth_Serial = serial.Serial(
		port='/dev/ttyAMA0', # SERIAL PORT on SBC 
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)
  ``` 
to run the motor A at 50% speed
``` python
motorA(50)
``` 
to run motor A in reverse direction at 25% speed
``` python
motorA(-25)
``` 
close serial after use
``` python
Sabertooth_Serial.close() 
```


``` python
import numpy as np
def calc_A(x):
    # motor A reference speed to byte (-100,0,100) -> (0,64,127) 
    return np.clip(int(x*0.630 + 64),1,127)

def calc_B(x):
    # motor B reference speed to byte (-100,0,100) -> (128,192,255)
    return np.clip(int(x*0.635 + 192),128,255)
```
