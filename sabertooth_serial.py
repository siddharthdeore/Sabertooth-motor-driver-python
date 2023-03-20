import serial

class SabertoothSerial:
    """Class for controlling a Sabertooth motor controller over a serial port."""

    def __init__(self, port, baudrate = 9600):
        """Initialize the SabertoothSerial object.

        Args:
            port (str): The name or path of the serial port to use (e.g. '/dev/ttyUSB0').

        Raises:
            serial.SerialException: If an error occurs while opening the serial port.
        """
        try:
            self.ser = serial.Serial(port=port,
                                     baudrate=baudrate,
                                     parity=serial.PARITY_NONE,
                                     stopbits=serial.STOPBITS_ONE,
                                     bytesize=serial.EIGHTBITS,
                                     timeout=1)
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")
            raise

    def __del__(self):
        """Close the serial port when the object is deleted."""
        if self.ser and self.ser.isOpen():
            self.ser.close()

    def lerp(self, x, in_min, in_max, out_min, out_max):
        """Interpolate the given value from one range to another.

        Args:
            x (int or float): The input value to interpolate.
            in_min (int or float): The minimum value of the input range.
            in_max (int or float): The maximum value of the input range.
            out_min (int or float): The minimum value of the output range.
            out_max (int or float): The maximum value of the output range.

        Returns:
            int: The interpolated value.

        """
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def motorA(self, speed):
        """Set the speed of motor A.

        Args:
            speed (int): The desired speed, between -100 and 100 inclusive.

        Raises:
            serial.SerialException: If an error occurs while writing to the serial port.

        """
        try:
            output = self.lerp(speed, -100, 100, 1, 128)
            self.ser.write(output.to_bytes(1,'little'))
        except serial.SerialException as e:
            print(f"Error writing to serial port: {e}")
            raise

    def motorB(self, speed):
        """Set the speed of motor B.

        Args:
            speed (int): The desired speed, between -100 and 100 inclusive.

        Raises:
            serial.SerialException: If an error occurs while writing to the serial port.

        """
        try:
            output = self.lerp(speed, -100, 100, 128, 256)
            self.ser.write(output.to_bytes(1,'little'))
        except serial.SerialException as e:
            print(f"Error writing to serial port: {e}")
            raise

    def drive(self, speedA, speedB):
        """Set the speeds of both motors.

        Args:
            speedA (int): The desired speed of motor A, between -100 and 100 inclusive.
            speedB (int): The desired speed of motor B, between -100 and 100 inclusive.

        Raises:
            serial.SerialException: If an error occurs while driving the motors.

        """
        try:
            self.motorA(speedA)
            self.motorB(speedB)
        except serial.SerialException as e:
            print(f"Error driving motors: {e}")
            raise
