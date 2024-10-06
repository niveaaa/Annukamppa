import serial
from datetime import date
import time
from emailattach import send_email
from report_generator import generate_report

# Define the serial port and baud rate
serial_port = 'COM3'  # Replace with your actual serial port (Windows: 'COMx')
baud_rate = 9600  # Must match the baud rate set in Arduino code
file = date.today()

# Open the CSV file for writing
with open(f'{file}.csv', 'a') as f:
    try:
        # Open serial port
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Serial port {serial_port} opened successfully.")

        while True:
            # Read data from serial port
            line = ser.readline().decode('utf-8').rstrip()
            if line:
                # Debugging output+
                print(f"Received: {line}")

                # Only process lines that have the format UID;Button
                if ';' in line:
                    try:
                        uid, button = line.split(';')
                        if uid == '3D67A7E5':
                            uid = 'Aditi'
                        elif uid == 'B04A5A7A':
                            uid = 'Jahanvi'
                        elif uid == 'FCE340C5':
                            uid = 'Bhavya'
                        elif uid == 'B0865A7A':
                            uid = 'Aarush'
                        elif uid == '496B9AE5':
                            uid = 'Aarshi'
                        elif uid == 'FBEEA4D5':
                            uid = 'Tvisha'
                        elif uid == '659B9AE5':
                            uid = 'Yash'
                        if button in ['Happy', 'Stressed', 'Sad', 'Angry']:
                            f.write(f'{uid},{button}\n')  # Write UID and Button to CSV
                            f.flush()  # Ensure data is written to the file
                            print(f"Saved to CSV: {uid},{button}")
                    except ValueError:
                        print(f"Line format is incorrect: {line}")

    except serial.SerialException as e:
        print(f"Error: {e}")

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

f.close()

report = generate_report()
send_email(report,f'{file}.csv')

