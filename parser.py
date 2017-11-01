# Parses Hack assembly text

import code
from code import AInstruction, CInstruction

class ParseError(Exception):
    pass

def __format_error(line_number, message, value):
    return str.format('Line {}: {} {}', line_number, value, message)

def __parse_a(line_number, line):
    _,  addr = line.split('@')
    try:
        addr = int(addr)
        #TODO check for upper address limit
        return AInstruction(addr)
    except ValueError:
        raise ParseError(__format_error(line_number, 'is not a valid address', addr))

def __parse_c(line_number, line):
    line = ''.join(line.split()) #remove all whitespace

    comp = line
    dest = None
    if '=' in comp:
        dest, comp = line.split('=')
        if dest not in code.C_DEST.keys():
            raise ParseError(__format_error(line_number, 'is not a valid destination', dest))

    jmp = None
    if ';' in comp:
        comp, jmp = comp.split(';')
        if jmp not in code.C_JUMP.keys():
            raise ParseError(__format_error(line_number, 'is not a valid jump operation', jump))

    if comp not in code.C_COMP.keys():
        raise ParseError(__format_error(line_number, 'is not a valid operation', comp))

    return CInstruction(dest, comp, jmp)

def parse(text):
    line_number = 0
    instructions = []
    for line in text:
        line_number += 1
        line = line.strip()
        if not line:
            continue
        elif line.startswith('//'):
            continue
        elif line.startswith('@'):
            instructions.append(__parse_a(line_number, line))
        else:
            instructions.append(__parse_c(line_number, line))
    return instructions
