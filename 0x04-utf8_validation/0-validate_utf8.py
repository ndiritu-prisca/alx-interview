#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    A method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    bit_1 = 1 << 7
    bit_2 = 1 << 6

    for i in data:

        msb = 1 << 7
        if number_bytes == 0:
            while msb & i:
                number_bytes += 1
                msb = msb >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & bit_1 and not (i & bit_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
