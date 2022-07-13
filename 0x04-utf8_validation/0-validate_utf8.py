#!/usr/bin/python3
'''validate if the data is valid utf-8 encoding'''


def validUTF8(data):
    '''determines if a given data set is valid UTF-8 encoding'''
    i = 0
    while i < len(data):
        try:
            if data[i] <= 0x7f:
                i += 1
            elif data[i] <= 0xdf and (0x80 <= data[i + 1] <= 0xbf):
                i += 2
            elif data[i] <= 0xef and (0x80 <= data[i + 1] <= 0xbf) and (
                    0x80 <= data[i + 2] <= 0xbf):
                i += 3
            elif data[i] <= 0xf7 and (0x80 <= data[i + 1] <= 0xbf) and (
                    0x80 <= data[i + 2] <= 0xbf) and (
                        0x80 <= data[i + 3] <= 0xbf):
                i += 4
            else:
                return False
        except IndexError:  # if no successive bytes
            return False
    return True
