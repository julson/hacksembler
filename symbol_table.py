import core
from core import ParseError

PREDEFINED_SYMBOLS = {
    'SP' : 0,
    'LCL' : 1,
    'ARG' : 2,
    'THIS' : 3,
    'THAT' : 4,
    'SCREEN' : 16384,
    'KBD' : 24576
}

for n in range(16):
    register = 'R' + str(n)
    PREDEFINED_SYMBOLS[register] = n

USER_SYMBOLS = {}

def add_label(instruction_count, name):
    if name in USER_SYMBOLS:
        raise ParseError(str.format('Duplicate label {} found', name))

    USER_SYMBOLS[name] = instruction_count
