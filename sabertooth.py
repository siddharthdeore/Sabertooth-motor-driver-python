import time
import serial
#interpolates the variable from input to output range
def lerp( x, min_in, max_in, min_out, max_out ):
	return min_out + (x - min_in) * (max_out-min_out)/(max_in-min_in)

#Rotates First Motor conected to M1A M1B of Sabertooth 2X25 or 2X60 Motor Driver
def driveA( speed ):
	output = lerp(speed, -100, 100, 0, 127)
	Sabertooth_Serial.write(output)
	
#Rotates Second Motor conected to M2A M2B of Sabertooth 2X25 or 2X60 Motor Driver
def driveB( speed ):
	output = lerp(speed, -100, 100, 128, 255)
	Sabertooth_Serial.write(output)

# Open Serial Port
try:
	Sabertooth_Serial = serial.Serial(
		port='/dev/ttyAMA0', # SERIAL PORT on SBC 
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
	)
	#Sabertooth_Serial = serial.Serial('/dev/ttyACM0',9600)	# Open Serial Port
	
	i=0
	j=0
	while 1:
		driveA(i)
		driveB(j)
		time.sleep(100)
		i += 1
		j -= 1
		
		if (i > 100 or j >100):
			i,j=j,i
			
	Sabertooth_Serial.close() # Close Serial Port
