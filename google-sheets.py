import serial
from datetime import date
from google.oauth2 import service_account
import gspread
from report_generator import generate_report
from emailattach import send_email
import pygame
import os

pygame.mixer.init()

# Define your Google Sheets credentials JSON file path
credentials_file = 'science.json'

# Define the scope of Google Sheets API you need to access
scope = ['https://www.googleapis.com/auth/spreadsheets']

# Authenticate using service account credentials
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, scopes=scope)

# Open Google Sheets client
gc = gspread.authorize(credentials)

# Open the specific Google Spreadsheet (replace with your spreadsheet ID)
spreadsheet_id = '1H7s8ONIxq9Fxk1ri8_u5y9x54w0Wsi-_SUC1x3u3Ygs'
sheet = gc.open_by_key(spreadsheet_id).sheet1  # Adjust sheet index if needed

# Define the serial port and baud rate
serial_port = 'COM3'  # Replace with your actual serial port (Windows: 'COMx')
baud_rate = 9600  # Must match the baud rate set in Arduino code

# Open serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)
print(f"Serial port {serial_port} opened successfully.")

#sheet.append_row([str(date.today())])
# sheet.append_row(['Student','Mood'])
scan_sound = 'scan.mp3'

try:
    while True:
        # Read data from serial port
        line = ser.readline().decode('utf-8').rstrip()
        if line:

            sound = pygame.mixer.Sound(scan_sound)
            sound.play()

            # Debugging output
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
                        uid = 'Bhavya'
                    elif uid == 'FBEEA4D5':
                        uid = 'Tvisha'
                    elif uid == '659B9AE5':
                        uid = 'Yash'
                    if button in ['Not Sure', 'Fine', 'Joyful', 'Sad']:
                        # Write to Google Spreadsheet
                        row = [uid, button]
                        sheet.append_row(row)
                        print(f"Saved to Google Spreadsheet: {row}")
                    print(uid)
                except ValueError:
                    print(f"Line format is incorrect: {line}")

except serial.SerialException as e:
    print(f"Error: {e}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    ser.close()
    print("Serial port closed.")

# Generate report and send email
report = generate_report()
send_email(report, 'Data from Arduino', attachment=None)  # You may attach the CSV file if needed