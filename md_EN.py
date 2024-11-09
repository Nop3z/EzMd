import serial
import time
import re

def dump_memory_test(start_address, end_address, chunk_size, serial_port, baud_rate, output_file):
    with serial.Serial(serial_port, baud_rate, timeout=2) as ser:
        with open(output_file, 'wb') as f:
            current_address = start_address
            while current_address < end_address:
                command = f"md {current_address:X} {chunk_size // 4:X}\n".encode('utf-8')
                ser.write(command)
                time.sleep(0.1)

                raw_output = b''
                while True:
                    line = ser.readline().decode('utf-8').strip()
                    if line == '':
                        break

                    match = re.search(r'^[0-9a-fA-F]{8}: ([0-9a-fA-F]{8} [0-9a-fA-F]{8} [0-9a-fA-F]{8} [0-9a-fA-F]{8})', line)
                    if match:
                        hex_data = match.group(1).replace(' ', '')
                        raw_output += bytes.fromhex(hex_data)

                if raw_output:
                    f.write(raw_output)
                    print(f"Read address: 0x{current_address:X}, Save data to {output_file}")

                current_address += chunk_size

if __name__ == '__main__':
    start_address = int(input("Please enter the start address(0):"), 16)
    end_address = int(input("Please enter the end address(30):"), 16)
    chunk_size = int(input("Please enter the block size(10):"))
    serial_port = input("Please enter the port number(COM 5):")
    baud_rate = int(input("Please enter baud rate(115200):"))
    output_file = input("Please enter the output file name(test.bin):")

    dump_memory_test(start_address, end_address, chunk_size, serial_port, baud_rate, output_file)