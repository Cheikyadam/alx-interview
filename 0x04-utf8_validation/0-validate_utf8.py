#!/usr/bin/python3
"""utf -8  validation"""


def validUTF8(data):
    """the function def"""
    def is_start_byte(byte):
        """Check if the byte is a valid start byte"""
        if byte >> 7 == 0:
            return 1
        elif byte >> 5 == 0b110:
            return 2
        elif byte >> 4 == 0b1110:
            return 3
        elif byte >> 3 == 0b11110:
            return 4
        return 0

    def is_continuation_byte(byte):
        """Check if the byte is a valid continuation byte"""
        return byte >> 6 == 0b10

    i = 0
    while i < len(data):
        start_byte = data[i]
        num_bytes = is_start_byte(start_byte)

        if num_bytes == 0:
            return False

        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_continuation_byte(data[i + j]):
                return False
        i += num_bytes
    return True
