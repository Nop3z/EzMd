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
                    print(f"读取地址: 0x{current_address:X}, 数据保存至 {output_file}")

                current_address += chunk_size

if __name__ == '__main__':
    start_address = int(input("请输入起始地址（16进制）："), 16)
    end_address = int(input("请输入结束地址（16进制）："), 16)
    chunk_size = int(input("请输入块大小（字节）："))
    serial_port = input("请输入串口号（例如COM3）：")
    baud_rate = int(input("请输入波特率（例如115200）："))
    output_file = input("请输入输出文件名（例如md.bin）：")

    dump_memory_test(start_address, end_address, chunk_size, serial_port, baud_rate, output_file)