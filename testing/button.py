import serial
from datetime import date

# Define the serial port and baud rate
serial_port = 'COM3'  # Replace with your actual serial port (Windows: 'COMx')
baud_rate = 9600  # Must match the baud rate set in Arduino code
file = date.today()

try:
    # Open serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Serial port {serial_port} opened successfully.")

    while True:
        # Read data from serial port
        line = ser.readline().decode('utf-8').rstrip()
        if line:
            print(f"Received: {line}")

            f = open(f'{file}.csv', 'a')
            f.write(f'{line}\n')

except serial.SerialException as e:
    print(f"Error: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")

f.close()
