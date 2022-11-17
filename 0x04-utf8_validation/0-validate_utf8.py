#!/usr/bin/python3
'''validate if the data is valid utf-8 encoding'''


def validUTF8(data):
    '''determines if a given data set is valid UTF-8 encoding'''
    i = 0
    while i < len(data):
        byte = data[i] & 0xff  # get 8 least significant bits

        def check_byte(b): return 0x80 <= data[b] <= 0xbf

        try:
            if byte <= 0x7f:
                i += 1
            elif byte <= 0xdf and check_byte(i + 1):
                i += 2
            elif byte <= 0xef and check_byte(i + 1) and check_byte(i + 2):
                i += 3
            elif byte <= 0xf7 and check_byte(i + 1) and check_byte(i + 2) and (
                    check_byte(i + 3)):
                i += 4
            else:
                return False
        except IndexError:  # if no successive bytes
            return False
    return True
