import serial

# Configure the serial port (adjust the port name and baud rate as needed)
# On Windows, it might be 'COM3', 'COM4', etc.
# On macOS/Linux, it might be '/dev/ttyUSB0', '/dev/ttyACM0', etc.
SERIAL_PORT = 'COM3'  # Replace with your serial port name
BAUD_RATE = 9600

# Open the serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

print("Listening for RFID cards...")

while True:
    try:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data.startswith("UID:"):
                uid = data[4:]  # Extract the UID after "UID:"
                print(f"Card UID: {uid}")
    except KeyboardInterrupt:
        print("Exiting...")
        break

ser.close()


