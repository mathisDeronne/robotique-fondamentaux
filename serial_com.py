#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

import serial


def open_serial(port, baud, timeout):
    ser = serial.Serial(port=port, baudrate=baud, timeout=timeout)
    if ser.isOpen():
        return ser
    else:
        print("SERIAL ERROR")


def close(ser):
    ser.close()


def write_data(ser, data):
    ser.write(data)


def read_data(ser, size=1):
    return ser.read(size)


def checksum(data):
    return TODO


# def bitwise_and_bytes(a, b):
#     result_int = int.from_bytes(a, byteorder="big") & int.from_bytes(b, byteorder="big")
#     return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

if __name__ == "__main__":
    # we open the port. Check that this is correct by running "ls /dev/ttyACM*" in a terminal
    serial_port = open_serial("/dev/ttyACM0", 1000000, timeout=0.1)

    on_or_off = 1
    # we create the packet for a LED ON/OFF command and alternate between them
    while True:
        # two start bytes
        data_start = 0xFF

        # id of the motor, you need to change it
        data_id = 53
        print(f"data_id raw = {data_id}")

        # Continue here the construction of the packet
        TODO

        # checksum (read the doc)
        data_checksum = checksum(
            TODO
        )  # 0xdd

        print("checksum = {}".format(data_checksum))

        # we concatenate everything into a bytes object
        list_of_integers = [
            TODO
        ]
        data = bytes(list_of_integers)

        print(f"to be send = {data}")

        write_data(serial_port, data)

        # read the status packet (size 6)
        d = read_data(serial_port, 6)
        # in_hex = hex(int.from_bytes(in_bin,byteorder='little'))
        # or in_hex = ser.read().hex()
        print(d)
        time.sleep(0.5)