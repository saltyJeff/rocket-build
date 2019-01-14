from typing import List
from struct import unpack
import binascii
from data_package import PACKAGE_CODE, PACKAGE_LEN

# Assumes a 4 byte FF delimiter between packages

parse_buffer: bytearray = bytearray(PACKAGE_LEN)
contig_ff = 0 #counts the number of contiguous FF's
write_index = PACKAGE_LEN #counts which index to write the next byte into
firstEncountered = False #throwaway the first data (is junk)
def parse_struct(bytes: bytearray) -> List[tuple]:
    if len(bytes) == 0:
        return []
    global write_index, contig_ff, firstEncountered
    tuple_list = []
    for b in bytes:
        if write_index < PACKAGE_LEN and firstEncountered:
            parse_buffer[write_index] = b
            write_index += 1
        elif b == 255:
            contig_ff += 1
            if contig_ff >= 4 and write_index == PACKAGE_LEN:
                if not firstEncountered:
                    firstEncountered = True
                else:
                    tuple_list.append(
                        unpack(PACKAGE_CODE, parse_buffer)
                    )
                contig_ff = 0 
                write_index = 0
        else:
            contig_ff = 0  
    return tuple_list