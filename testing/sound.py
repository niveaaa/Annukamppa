import pygame
import serial
import os

# Initialize the mixer
pygame.mixer.init()

serial_port = 'COM3'  # Replace with your actual serial port (Windows: 'COMx')
baud_rate = 9600  # Must match the baud rate set in Arduino code

# Open serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)
print(f"Serial port {serial_port} opened successfully.")

while True:
    # Read data from serial port
    line = ser.readline().decode('utf-8').rstrip()
    if line:
        # Construct the file path
        sound_file = f'sounds/{line}.mp3'
        
        # Check if the sound file exists
        if os.path.isfile(sound_file):
            # Load the sound file
            sound = pygame.mixer.Sound(sound_file)
            # Play the sound
            sound.play()
        else:
            print(f"Sound file {sound_file} does not exist.")
