#!/usr/bin/python3
"""Defines a method to verify if a data set represents a
   valid UTF-8 encoding
"""


def validUTF8(data):
    """Check if a list of integers follows the UTF-8 encoding rules"""
    n_bytes = 0

    # For the first bit is 1 in the binary representation
    # of mask and num and check if they are the same
    mask1 = 1 << 7

    # For the second bit is 1 in the binary representation of mask2
    mask2 = 1 << 6
    for num in data:

        # The num with the first bit only
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters
            if n_bytes == 0:
                continue

            # Invalid scenario according to the rules
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If it is not of pattern 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1

    # This is to check if we have some left over bytes which were not needed
    return n_bytes == 0
