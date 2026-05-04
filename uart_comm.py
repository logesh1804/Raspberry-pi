import serial
import time

# Open UART port
ser = serial.Serial(
    port='/dev/serial0',  # Raspberry Pi UART
    baudrate=9600,
    timeout=1
)

time.sleep(2)  # Wait for connection

print("UART Communication Started...")

while True:
    # Send data
    message = "Hello Device\n"
    ser.write(message.encode())
    print("Sent:", message.strip())

    # Receive data
    if ser.in_waiting > 0:
        received = ser.readline().decode().strip()
        print("Received:", received)

    time.sleep(2)
